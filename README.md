# Codetrellis

**Code editing. Redefined.**

Codetrellis is a free, open-source code editor built from [Code - OSS](https://github.com/microsoft/vscode) (the MIT-licensed core of Visual Studio Code). It combines the simplicity of a code editor with everything developers need for their core edit-build-debug cycle — comprehensive code editing, navigation, and understanding support along with lightweight debugging, a rich extensibility model, and lightweight integration with existing tools.

## The Repository

This repository is where Codetrellis is developed. The source code is available to everyone under the [MIT license](LICENSE.txt).

**Upstream:** This project is a fork of [microsoft/vscode](https://github.com/microsoft/vscode) (Code - OSS).

## Key Differences from Code - OSS

- **Branding:** Product name, identifiers, and bundle IDs are Codetrellis
- **Extension Gallery:** Points to [Open VSX](https://open-vsx.org) (not Microsoft Marketplace)
- **Telemetry:** Disabled by default
- **No AI features:** Default chat agent configuration removed

## Contributing

There are many ways in which you can participate in this project:

- [Submit bugs and feature requests](https://github.com/keshav4u/codetrellis-ide/issues)
- Review [source code changes](https://github.com/keshav4u/codetrellis-ide/pulls)

If you are interested in fixing issues and contributing directly to the code base, please see [CONTRIBUTING.md](CONTRIBUTING.md).

## Bundled Extensions

Codetrellis includes a set of built-in extensions located in the [extensions](extensions) folder, including grammars and snippets for many languages. Extensions that provide rich language support (inline suggestions, Go to Definition) for a language have the suffix `language-features`. For example, the `json` extension provides coloring for `JSON` and the `json-language-features` extension provides rich language support for `JSON`.

## Building from Source

### Prerequisites

- Git
- Node.js (LTS recommended)
- Python 3
- Platform-specific build tools (Xcode CLI on macOS, build-essential on Linux, VS Build Tools on Windows)

### Build & Run

```bash
npm install
npm run watch    # in one terminal
npm run electron # in another terminal
```

See upstream [How to Contribute](https://github.com/microsoft/vscode/wiki/How-to-Contribute) for detailed build instructions.

## License

Copyright (c) Microsoft Corporation. All rights reserved.
Modifications copyright (c) Codetrellis.

Licensed under the [MIT](LICENSE.txt) license.

See [NOTICE](NOTICE) for upstream attribution.
