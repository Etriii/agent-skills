# Repository instructions

## Installation documentation and recommendations

- Lead skill installation guidance with the supported direct `npx skills@1.7.4 add` route. Ordinary skills do not require the user to clone or manually download this collection. Preserve the Python installer as an explicitly optional recorded/offline route.
- State prerequisites before commands: Node.js 22.20+ with npm/npx, network access for remote sources, and Git for repository fallback. Distinguish installer requirements from the selected skill's runtime requirements.
- Give commands in separate fenced lines. Label shell and starting folder, show actual project-versus-global scope, identify every placeholder to replace, explain agent selection, expected installed files, session refresh, and the separate chat invocation.
- `npx` uses `--agent codex claude-code` for both agents; the Python installer uses `--agent both`. Never transfer flags between their interfaces. Do not add global scope or noninteractive approval flags without the user's intended scope.
- Explain Ultimate QA core/client support files explicitly: retain a durable matching kit and its helpers/templates, set `ULTIMATE_QA_KIT` for external installs, and keep application targeting separate from the kit directory. Curl can download the complete ZIP before an npx install from that same snapshot; a manual Git clone is optional.
- Before any `python tools/install_skills.py` example, explain how to obtain the complete checkout/ZIP, how to find its root containing `tools/` and `packs/`, and which directory the command runs from. The script is a local file, not a globally available command. Show dry-run and changing commands separately and explain their effects.
- Preserve the installer's ownership, backups and Markdown-history behavior. Use the installer that owns a copy for update/removal; recommending npx does not migrate existing Python-managed copies or grant permission to install anything.
- Remote commands use published files, not local unpushed edits. Explain missing/unpublished skill names and local-source alternatives without claiming publication or silently changing sources. No curl-to-shell installer is shipped; do not invent one.
- Keep READMEs, INSTALL.md, the npx guide, contribution/pack-authoring guidance, relevant skill docs and payload manifests consistent. Follow the command documentation contract in CONTRIBUTING.md and run the relevant checks. Historical evidence keeps its original facts and names.
