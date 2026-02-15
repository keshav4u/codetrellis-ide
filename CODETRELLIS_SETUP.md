You are a long-running software engineering agent working in my local workspace.

## Mission

# Codetrellis — Code-OSS Fork Setup (Build, Run, Test)

> **Purpose:** This guide is for forking **Code - OSS** (the MIT-licensed open-source core of VS Code), rebranding it to **Codetrellis**, building it locally, and running/testing the editor.
>
> **Scope:** Fork + branding + build + run + packaging basics. No AI features.

---

## 0) Prerequisites

### macOS (your current environment)

- **Git**
- **Node.js** (LTS recommended)
- **Yarn** (used by upstream VS Code build scripts)
- **Python 3**
- **Xcode Command Line Tools**

### Windows / Linux (if you build there)

- Windows: Visual Studio Build Tools (C++), Python 3
- Linux: build tools (`build-essential`/`clang`), Python 3

> Reality check: the exact versions/steps change by Code-OSS commit. Once you pin the upstream commit, read that commit’s build docs and align Node/Yarn versions accordingly.

---

## 1) Legal + compliance (MIT + branding)

### 1.1 What you’re allowed to do under MIT

With Code-OSS (MIT), you may:

- Copy, modify, and distribute the software.
- Ship it commercially.

### 1.2 What you MUST keep when distributing

When you distribute source or binaries that include Code-OSS code:

- ✅ Keep the **MIT license text** and upstream copyright notices.
- ✅ Include required **third-party notices** for dependencies you ship.

### 1.3 What you should remove/replace (trademarks + service terms)

MIT does **not** grant Microsoft trademark rights and does not grant access to Microsoft-hosted services.

Replace/remove:

- ❌ “Visual Studio Code” / “VS Code” naming and logos
- ❌ Microsoft identifiers (bundle IDs, app IDs, update IDs)
- ❌ Microsoft Visual Studio Marketplace endpoints (use Open VSX or your own)
- ❌ Microsoft telemetry endpoints (disable or replace)

### 1.4 Minimal NOTICE template (Codetrellis)

Create a `NOTICE` file in your distribution:

```text
Codetrellis

This product includes software from “Code - OSS” (the open source core of Visual Studio Code)
licensed under the MIT License.

Upstream source: https://github.com/microsoft/vscode
License: MIT

This distribution includes modifications by Codetrellis.
```

---

## 2) Fork Code-OSS

1. Fork upstream Code-OSS:
   - https://github.com/microsoft/vscode
2. Clone your fork locally.
3. **Pin a baseline** (tag or commit SHA) and record it.
   - This matters for reproducible builds.

---

## 3) Rebrand to Codetrellis (first PR should be branding-only)

Make your first change-set _only_ about naming/branding/endpoints.

### 3.1 What to change

- Product name: **Codetrellis**
- Executable name (optional, but recommended)
- App icon(s)
- Bundle identifiers (macOS) / app IDs (Windows)
- Update channel/product IDs
- Extension gallery configuration (avoid Microsoft Marketplace)
- Telemetry defaults + endpoints

### 3.2 Where to look (because paths move across upstream versions)

Search in your fork for these terms and update each occurrence appropriately:

- `Visual Studio Code`
- `VS Code`
- `Microsoft`
- `vscode` (product identifiers, not necessarily source folder names)
- `extensionGallery`
- `marketplace`
- `telemetry`

Typical hotspots include (names may vary by version):

- `product.json` (or product configuration)
- `resources/` (icons, branding)
- `build/` (package identities)

### 3.3 Marketplace (extensions)

By default, do **not** use Microsoft’s Visual Studio Marketplace endpoints.

Common approach for forks:

- Point the extension gallery to **Open VSX**

---

## 4) Build + run (developer mode)

> Build instructions change over time; always prefer the docs in the upstream repo at the commit you pinned.

Below are **typical** commands used in the Code-OSS workflow.

### 4.1 Install dependencies

```zsh
yarn
```

### 4.2 Start the editor from source

Common dev loops include:

```zsh
yarn watch
```

In another terminal:

```zsh
yarn run electron
```

If your pinned version differs, follow the repo’s “How to Run” / “Development” docs.

---

## 5) Package the editor (optional)

Packaging differs by OS and upstream version. Look for packaging scripts under `build/`.

Typical result artifacts:

- macOS: `.app` (optionally `.dmg`)
- Windows: installer + portable zip
- Linux: `.deb` / `.rpm` / `.tar.gz`

---

## 6) Quick verification checklist

After you can launch the editor, verify:

- About dialog shows **Codetrellis** (not VS Code)
- App icon is Codetrellis
- Extension gallery is **not** Microsoft Marketplace
- Telemetry is disabled by default (or uses Codetrellis endpoint if explicitly enabled)

---

## 7) If you want this to become “exact commands”

Once you add your actual Code-OSS fork into this workspace (so we can see the pinned commit and scripts), I can update this document to include:

- the exact Node/Yarn versions for that commit
- the exact build/run/package commands for macOS
- the exact files/keys you should change for Codetrellis branding

## Required Session Artifacts

Update every session:

- `docs/sessions/SESSION_LATEST.md` (overwrite)
- `docs/sessions/STATUS.md` (rolling)
- `docs/sessions/CHANGELOG_SESSION.md` (append)
