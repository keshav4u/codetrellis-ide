# Codetrellis — Session Changelog

## 2026-02-15 — Initial Setup & Branding

### Added
- `NOTICE` — MIT license attribution file for Code-OSS upstream
- `docs/sessions/SESSION_LATEST.md` — Session report
- `docs/sessions/STATUS.md` — Rolling project status
- `docs/sessions/CHANGELOG_SESSION.md` — This file

### Changed
- `product.json` — Full rebrand from "Code - OSS" to "Codetrellis":
  - Product names (`nameShort`, `nameLong`, `applicationName`)
  - Data folder (`.vscode-oss` → `.codetrellis`)
  - macOS bundle identifier (`com.visualstudio.code.oss` → `com.codetrellis.ide`)
  - Windows identifiers (DirName, NameVersion, RegValue, AppUserModelId, ShellName, mutexes)
  - Server/tunnel application names
  - Linux icon name
  - URL protocol (`code-oss` → `codetrellis`)
  - Report issue URL → `keshav4u/codetrellis-ide`
  - License URLs → `keshav4u/codetrellis-ide`
  - Added `extensionGallery` pointing to Open VSX
  - Added `enableTelemetry: false`
  - Added `extensionEnabledApiProposals: {}`
  - Removed `defaultChatAgent` (Copilot configuration)
  - Simplified `trustedExtensionAuthAccess` to empty object
  - Cleared `webviewContentExternalBaseUrlTemplate` (Microsoft CDN)
- `package.json`:
  - `name`: `code-oss-dev` → `codetrellis`
  - `author.name`: `Microsoft Corporation` → `Codetrellis`

### Infrastructure
- Cloned `microsoft/vscode` at commit `d057f3f`
- Set up remotes: `origin` (keshav4u/codetrellis-ide), `upstream` (microsoft/vscode)
- Created branch `codetrellis/main`
- Installed Node.js v22.22.0 via nvm
- Started `npm install` (dependencies)
