# Codetrellis — Project Status

**Last Updated:** 2026-02-15 (Session 2)

## Current State: ✅ Branding Complete + Build Verified

### Completed

- [x] Repository cloned from upstream Code-OSS
- [x] Remotes configured (origin → keshav4u/codetrellis-ide, upstream → microsoft/vscode)
- [x] Branch `codetrellis/main` created
- [x] NOTICE file created (MIT compliance)
- [x] product.json fully rebranded to Codetrellis
- [x] package.json name/author updated
- [x] Extension gallery pointed to Open VSX
- [x] Microsoft telemetry disabled
- [x] defaultChatAgent (Copilot) config removed
- [x] `npm install` — 1,498 packages installed successfully
- [x] `npm run watch` — transpilation 0 errors, TS compilation 0 errors
- [x] `npm run electron` — Electron downloaded, binary named `Codetrellis`
- [x] App launched as `Codetrellis.app` — verified working
- [x] Git commit `34110ad` on `codetrellis/main`
- [x] README.md — complete rewrite for Codetrellis
- [x] CONTRIBUTING.md — complete rewrite for Codetrellis
- [x] SECURITY.md — rebranded with Codetrellis security policy
- [x] Windows installer ISL files (13 locales) — "Visual Studio Code" → "Codetrellis"
- [x] macOS signing plist descriptions — "Visual Studio Code" → "Codetrellis"
- [x] build/builtin/browser-main.js — `.vscode-oss-dev` → `.codetrellis-dev`
- [x] All build/test package.json + lock files — `code-oss-dev-*` → `codetrellis-*`
- [x] Linux appdata.xml — summary, description, homepage updated
- [x] Linux desktop files — Keywords updated to `codetrellis`
- [x] Linux debian control.template — maintainer, homepage, description updated
- [x] Linux debian templates.template — description updated
- [x] Linux debian postinst.template — skips Microsoft apt repo for Codetrellis
- [x] Linux debian postrm.template — uses codetrellis.sources/gpg
- [x] Linux RPM spec — vendor, packager, URL, description updated
- [x] Linux snap snapcraft.yaml — description updated
- [x] extensions/package.json — `vscode-extensions` → `codetrellis-extensions`
- [x] Build verification — VS Code - Build task: 0 errors across all 3 tasks

### In Progress

- [ ] Push to origin (unshallowing history to resolve pack error)

### Pending

- [ ] Custom app icons (design task)

## Key Decisions

| Decision                                  | Rationale                                                          |
| ----------------------------------------- | ------------------------------------------------------------------ |
| Open VSX for extensions                   | Avoid Microsoft Marketplace trademark/ToS issues                   |
| Telemetry disabled by default             | Privacy-first for fork users                                       |
| Removed defaultChatAgent                  | No AI features in scope per mission                                |
| Kept builtInExtensions                    | js-debug etc. are MIT-licensed, needed for dev experience          |
| Kept Microsoft copyright headers          | Required by MIT license                                            |
| Kept VSCODE\_\* env vars in shell scripts | Internal variable names used by Electron, not user-facing branding |

## Baseline

- **Upstream commit:** `d057f3f` — "Fix hook cwd resolution in multi-root workspaces (#295365)"
- **Electron:** v39.5.2
- **Node.js:** v22.22.0
- **npm:** 10.9.4
