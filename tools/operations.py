"""Commit validated local payloads and their ownership records in one transaction."""

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
from uuid import UUID, uuid5

from catalog import NAME, digest, safe_path
from records import SKILL_TARGET, STATE, inventory, new_event, read_record, staged_record
from transaction import BACKUPS, TRANSACTION, install


def commit(root, plans, *, transaction_id=None):
    """Guard current ownership and publish every operation with its payload swaps."""
    from contextlib import ExitStack

    root = safe_path(root)
    if safe_path(root / TRANSACTION).exists():
        raise ValueError("Pending collection transaction; inspect recovery before another operation")
    owners, sequence = inventory(root)
    state = safe_path(root / STATE)
    guards = {state: digest(state) if state.exists() else None}
    copies, additions, events, seen = [], {}, [], set()
    for offset, plan in enumerate(plans, 1):
        if not plan['entries']:
            raise ValueError("An operation must contain reviewed entries")
        pack = plan['pack']
        if not NAME.fullmatch(pack) or plan['agent'] not in {'codex', 'claude', 'both'} or plan['scope'] not in {'project', 'user'}:
            raise ValueError("Invalid local operation identity")
        event = new_event(sequence=sequence + offset, operation=plan['operation'], pack=pack,
                          agent=plan['agent'], scope=plan['scope'], root=str(root), source=plan['source'],
                          manifest_sha256=plan['manifest_sha256'], entries=deepcopy(plan['entries']), backup=None)
        if plan.get('id'):
            event['id'] = UUID(plan['id']).hex
        plan_copies = {target.relative_to(root).as_posix(): (source, target, before, after)
                       for source, target, before, after in plan['copies']}
        if len(plan_copies) != len(plan['copies']):
            raise ValueError("Duplicate operation copy target")
        for entry in event['entries']:
            relative = entry['target']
            if not SKILL_TARGET.fullmatch(relative) or relative in seen:
                raise ValueError("Invalid or duplicate operation target")
            seen.add(relative)
            target = safe_path(root / relative)
            owner = owners.get(relative)
            if entry['installed_record'] != (owner['record'] if owner else None) or (owner and owner['pack'] != pack):
                raise ValueError("Ownership changed since preview")
            actual = digest(target) if target.exists() else None
            if actual != entry['before'] or (owner and actual not in {None, owner['digest']} and entry['action'] != 'REPLACE WITH BACKUP'):
                raise ValueError("Destination changed since preview")
            guards[target] = actual
            if relative in plan_copies:
                source, _, before, after = plan_copies.pop(relative)
                if (before, after) != (entry['before'], entry['after']):
                    raise ValueError("Copy and ownership evidence disagree")
                if before is not None:
                    event['backup'] = str(root / BACKUPS / (transaction_id or event['id']))
                    entry['backup_path'] = str(Path(event['backup']) / 'backups' / str(len(copies)))
                copies.append((source, target, before, after))
            elif entry['before'] != entry['after']:
                raise ValueError("Changing entry has no matching payload operation")
        if plan_copies:
            raise ValueError("Payload copy lacks ownership evidence")
        for target, expected in plan.get('guards', {}).items():
            if target in guards and guards[target] != expected:
                raise ValueError("Inconsistent operation guard")
            guards[target] = expected
        additions.update(plan.get('additions', {}))
        events.append(event)
    if not events:
        return []
    identity = transaction_id or events[0]['id']
    with ExitStack() as stack:
        for event in events:
            record = stack.enter_context(staged_record(event))
            target = root / STATE / 'history' / event['id']
            if target.exists():
                raise ValueError("Operation ID already exists; verify its committed result before retrying")
            copies.append((record, target, None, digest(record)))
        install(root, copies, additions=additions, guards=guards, transaction_id=identity)
    return events


def payload_operation_id(transaction_id, pack):
    """Derive stable per-pack event identities for a recoverable caller operation."""
    return uuid5(UUID(transaction_id), pack).hex


def install_payloads(root, rows, *, transaction_id):
    """Install reviewed local trees without executing their instructions or hooks."""
    root = safe_path(root)
    UUID(transaction_id)
    if safe_path(root / TRANSACTION).exists():
        raise ValueError("Pending collection transaction; inspect --recover before retrying")
    owners, _ = inventory(root)
    groups, targets = {}, set()
    for row in rows:
        name, agent, pack = row['name'], row['agent'], row['provider_pack']
        if not NAME.fullmatch(name) or len(name) > 64 or not NAME.fullmatch(pack) or agent not in {'codex', 'claude'}:
            raise ValueError("Invalid reviewed payload identity")
        relative = ('.agents' if agent == 'codex' else '.claude') + '/skills/' + name
        if row['installed_path'] != relative or relative in targets:
            raise ValueError("Invalid or duplicate reviewed payload destination")
        targets.add(relative)
        source = safe_path(Path(row['source']))
        if source == root or source in root.parents or source == root / relative or root / relative in source.parents:
            raise ValueError("Payload source overlaps destination")
        if digest(source) != row['after']:
            raise ValueError("Reviewed payload source changed")
        groups.setdefault(pack, []).append(row)
    plans, result, existing = [], {}, []
    for pack, group in sorted(groups.items()):
        identity = payload_operation_id(transaction_id, pack)
        agents = {row['agent'] for row in group}
        agent = 'both' if len(agents) == 2 else next(iter(agents))
        # This is the actual reviewed payload-plan fingerprint, not a vendor manifest claim.
        manifest = sha256(json.dumps([{key: row[key] for key in ('source', 'installed_path', 'after')}
                                     for row in sorted(group, key=lambda item: item['installed_path'])], sort_keys=True).encode()).hexdigest()
        event_path = safe_path(root / STATE / 'history' / identity / 'operation.md')
        if event_path.exists():
            event = read_record(event_path)
            expected = {row['installed_path']: row for row in group}
            if (event['pack'] != pack or event['root'] != str(root) or event['scope'] != 'project'
                    or event['operation'] != 'install' or event['agent'] != agent or event['manifest_sha256'] != manifest
                    or len(event['entries']) != len(expected)):
                raise ValueError("Committed payload operation differs from approved intent")
            for entry in event['entries']:
                row = expected.get(entry['target'])
                owner = owners.get(entry['target'])
                if (row is None or entry['before'] != row['before'] or entry['after'] != row['after']
                        or not owner or owner['record'] != identity or owner['digest'] != row['after']
                        or digest(safe_path(root / entry['target'])) != row['after']):
                    raise ValueError("Committed payload or ownership changed; preserve developer edits")
                result[entry['target']] = identity
            existing.append(True)
            continue
        existing.append(False)
        entries, copies, guards = [], [], {}
        for row in group:
            target = safe_path(root / row['installed_path'])
            before = digest(target) if target.exists() else None
            owner = owners.get(row['installed_path'])
            if before != row['before'] or (owner and owner['pack'] != pack):
                raise ValueError("Reviewed destination or pack ownership changed")
            if owner and before not in {None, owner['digest']}:
                raise ValueError("Modified managed destination preserved")
            guards[target] = before
            action = 'ADOPT MATCHING COPY' if before == row['after'] else 'REPLACE WITH BACKUP' if before is not None else 'COPY'
            if before != row['after']:
                copies.append((Path(row['source']), target, before, row['after']))
            entries.append(dict(target=row['installed_path'], action=action, before=before, after=row['after'],
                                installed_record=owner['record'] if owner else None, backup_path=None))
            result[row['installed_path']] = identity
        plans.append(dict(id=identity, pack=pack, agent=agent, scope='project', operation='install',
                          source='reviewed-local-payload-plan', manifest_sha256=manifest, entries=entries,
                          copies=copies, additions={}, guards=guards))
    if any(existing) and not all(existing):
        raise ValueError("Incomplete multi-pack ownership history; inspect the original transaction")
    if plans:
        commit(root, plans, transaction_id=transaction_id)
    return result
