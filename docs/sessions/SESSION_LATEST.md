# Codetrellis — Session Report (Latest)

**Date:** 2026-02-15 (Session 2)
**Branch:** `codetrellis/main`
**Baseline Commit:** `d057f3f` (upstream `microsoft/vscode` main)

---

## What Was Done

### Session 1 (Initial Setup) — Completed

- Repository cloned, remotes configured, branch created
- NOTICE file created (MIT compliance)
- `product.json` fully rebranded (names, IDs, gallery, telemetry)
- `package.json` name/author updated
- Build verified (0 errors), Electron downloaded, app launched as `Codetrellis.app`

### Session 2 (Complete Branding Sweep) — This Session

#### 1. README.md — Complete Rewrite

- Replaced entire upstream VS Code README with Codetrellis-branded version
- Removed Microsoft badges, links, and branding
- Added fork attribution, key differences section, build instructions

#### 2. CONTRIBUTING.md — Complete Rewrite

- Replaced upstream VS Code contributing guide with Codetrellis version
- Updated issue/PR links to keshav4u/codetrellis-ide
- Added upstream attribution section

#### 3. SECURITY.md — Rebranded

- Replaced Microsoft security policy with Codetrellis security reporting guide
- Points to GitHub Security Advisories for the fork
- References upstream MS security for core editor issues

#### 4. Windows Installer Messages (build/win32/i18n/)

- Updated all 13 ISL locale files (en, de, fr, es, it, ja, ko, pt-br, ru, tr, hu, zh-cn, zh-tw)
- Replaced "Visual Studio Code" → "Codetrellis" in update progress strings

#### 5. macOS Signing (build/darwin/sign.ts)

- Updated all 4 plist privacy descriptions:
  - AppleScript, Microphone, Camera, Audio Capture
  - "Visual Studio Code" → "Codetrellis"

#### 6. Build Scripts

- `build/builtin/browser-main.js`: `.vscode-oss-dev` → `.codetrellis-dev`
- `build/package.json`: `code-oss-dev-build` → `codetrellis-build`
- `build/package-lock.json`: name updated
- `build/npm/gyp/package.json` + lock: name updated

#### 7. Linux Packaging

- `resources/linux/code.appdata.xml`: Updated summary, description, homepage; removed Microsoft screenshot URL
- `resources/linux/code.desktop`: `Keywords=vscode` → `Keywords=codetrellis`
- `resources/linux/code-url-handler.desktop`: Same keyword fix
- `resources/linux/debian/control.template`: Updated maintainer, homepage, description
- `resources/linux/debian/templates.template`: Updated description text
- `resources/linux/debian/postinst.template`: Skip Microsoft apt repo for `codetrellis` builds
- `resources/linux/debian/postrm.template`: `vscode.sources` → `codetrellis.sources`, `microsoft.gpg` → `codetrellis.gpg`
- `resources/linux/rpm/code.spec.template`: Updated vendor, packager, URL, description
- `resources/linux/snap/snapcraft.yaml`: Updated description

#### 8. Test Package Names

- `test/smoke/package.json`: `code-oss-dev-smoke-test` → `codetrellis-smoke-test`
- `test/sanity/package.json`: `code-oss-dev-sanity-test` → `codetrellis-sanity-test`
- `test/integration/browser/package.json` + lock: `code-oss-dev-integration-test` → `codetrellis-integration-test`
- `test/mcp/package.json`: `code-oss-dev-mcp` → `codetrellis-mcp`

#### 9. Extensions

- `extensions/package.json`: `vscode-extensions` → `codetrellis-extensions`

#### 10. Build Verification

- `VS Code - Build` task: **0 errors** (Core - Transpile, Core - Typecheck, Ext - Build)

---

## Branding Audit Summary

| Area                                            | Status                   |
| ----------------------------------------------- | ------------------------ |
| `product.json` — names, IDs, gallery, telemetry | ✅ Complete (Session 1)  |
| `package.json` — root name/author               | ✅ Complete (Session 1)  |
| `README.md`                                     | ✅ Complete (Session 2)  |
| `CONTRIBUTING.md`                               | ✅ Complete (Session 2)  |
| `SECURITY.md`                                   | ✅ Complete (Session 2)  |
| `NOTICE` file                                   | ✅ Complete (Session 1)  |
| Windows installer messages (13 ISL files)       | ✅ Complete (Session 2)  |
| macOS signing plist strings                     | ✅ Complete (Session 2)  |
| Linux packaging (deb/rpm/snap/appdata/desktop)  | ✅ Complete (Session 2)  |
| Build script names (package.json files)         | ✅ Complete (Session 2)  |
| Test package names                              | ✅ Complete (Session 2)  |
| Extension gallery → Open VSX                    | ✅ Complete (Session 1)  |
| Telemetry disabled                              | ✅ Complete (Session 1)  |
| defaultChatAgent removed                        | ✅ Complete (Session 1)  |
| Custom app icons                                | ⬜ Pending (design task) |

## Known Remaining References (Intentionally Kept)

- `builtInExtensions` in `product.json` reference `ms-vscode.*` repos — these are MIT-licensed upstream dependencies, names are package identifiers not branding
- `build/lib/test/fixtures/policies/` — test fixtures with `Code - OSS` policy names (internal test data, not user-facing)
- Copyright headers `Copyright (c) Microsoft Corporation` — required by MIT license, must be preserved
- `resources/linux/snap/electron-launch` — has `VSCODE_*` env vars used by Electron internals
- `resources/linux/bin/code.sh` — has `VSCODE_PATH` used as internal variable names

## Open Items

- [ ] Custom app icons (design task — placeholder icons still from upstream)
- [ ] Push to `origin` (unshallowing may still be needed)

## Environment

- macOS (Apple Silicon)
- Node.js v22.22.0, npm 10.9.4
- Git 2.51.1
- Python 3.14.0
