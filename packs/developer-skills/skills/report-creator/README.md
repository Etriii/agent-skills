# Report Creator

Discover reporting needs across an application, specify useful business reports, and implement role-aware report pages with styled PDF and Excel exports.

## Use

Run these in agent chat from the target application, or include its path:

```text
$report-creator scan
$report-creator scan inventory and sales
$report-creator plan sales --detail mid
$report-creator plan sales --detail detailed
$report-creator build sales --detail detailed
$report-creator verify sales
$report-creator help
```

Claude Code uses `/report-creator` with the same arguments. These are instructions to the agent, not terminal commands. Bare invocation scans; the default report detail is `mid`. Scan and plan are read-only unless a saved artifact is requested. Build implements only the selected scope and does not require repeating existing authorization.

Mid reports contain core figures, meaningful status/type counts, essential records, and metric notes. Detailed reports add supported analysis, exceptions, reconciliation, drilldowns, and fuller explanations. Both levels require effective-filter disclosure, role and data isolation, clean PDF and actual `.xlsx` exports, and retained generated files.

PDFs start with a system/organization cover, contents from page two, then a separate summary and report sections. Workbooks use Cover, Contents, Summary, Breakdowns, record sheets, and Reading Notes. Status/type colors follow the application's palette across screen and exports; counts reflect the full matching scope.

A dedicated Generated Reports page lists files available to their authorized audiences. Default availability is 24 hours from successful generation, configurable through backend settings or environment configuration. Shared downloads require access to every included section, record scope, and field; matching role names alone are insufficient.

Read the [agent instructions](SKILL.md) for command boundaries and linked discovery, document, access, lifecycle, and verification guidance.

## Install

PowerShell, starting in the local collection root; Python 3.11+:

```powershell
python tools/install_skills.py --pack developer-skills --agent both --project "D:\My App" --skills report-creator --dry-run
python tools/install_skills.py --pack developer-skills --agent both --project "D:\My App" --skills report-creator
```

Preview should select only this skill for both agents. The changing command uses the installer's existing confirmation and records. Choose `--agent codex` or `--agent claude` for one agent. Refresh the agent session after installation.

For a published copy, the external CLI can install it with Node.js 22.20+ and npm:

```powershell
npx skills@1.7.4 add https://github.com/Etriii/agent-skills --skill report-creator --agent codex --copy
```

Run from the target application for project scope. The remote command requires the change to have been published; a local merge does not publish it. See the [pack guide](../../README.md), [installation options](../../../../INSTALL.md), [npx guide](../../../../docs/NPX_INSTALLATION.md), and [removal guide](../../../../UNINSTALL.md).

## Prerequisites and evidence limits

Provide source access and the reporting scope. Runtime verification additionally needs the application's normal database, test tools, PDF/Excel libraries, worker, storage, scheduler, and permitted test accounts as applicable. Reuse installed tools; this skill adds no runtime dependencies or environment keys of its own.

Missing policy, source fields, historical data, rendering tools, roles, or runtime services remain explicit gaps. Static inspection, installation, and passing tests do not prove visual quality, model adherence, scheduled cleanup, or production behavior. Compatibility metadata records only verified native agent discovery.

License status remains [UNDECIDED](../../../../LICENSE.md). Follow the [contribution guide](../../../../CONTRIBUTING.md).
