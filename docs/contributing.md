---
title: Contributing guidelines
permalink: /contributing/
relative_path: pages/contributing.md
layout: page
---

# Contributing guidelines

[![Codacy quality grade](https://app.codacy.com/project/badge/Grade/3f55a14f5dc14a0eba41f86006c1185b)](https://app.codacy.com/gh/facioquo/stock-indicators-python/dashboard)
[![Codacy code coverage](https://app.codacy.com/project/badge/Coverage/3f55a14f5dc14a0eba41f86006c1185b)](https://app.codacy.com/gh/facioquo/stock-indicators-python/dashboard)

**Thanks for taking the time to contribute!**

This project is simpler than most, so it's a good place to start contributing to the open source community, even if you're a newbie.

We are accepting these sorts of changes and requests:

- Bug reports and fixes
- Usability improvements
- Documentation updates
- New reputable "by the book" indicators and overlays

We are not accepting things that should be done in your own wrapper code:

- Personal customizations and preferences
- Modified or augmented outputs that are not intrinsic

## Reporting bugs and feature requests

We have different places to take issues by its category.

### Bug Report

If you are reporting a bug or suspect a problem, please submit an issue with a detailed description of the problem + include steps to reproduce, code samples, and any reference materials.

🔧 [Report bugs](https://github.com/facioquo/stock-indicators-python/issues/new?labels=bug&template=bug_report.md)

### Feature Request

For new features, submit an issue with the `enhancement` label.

💡 [Request features](https://github.com/facioquo/stock-indicators-python/issues/new?labels=enhancement&template=feature_request.md)

## Project management

- Planned work is managed in [the backlog](https://github.com/users/DaveSkender/projects/2).
- Work items are primarily [entered as Notes](https://docs.github.com/issues/organizing-your-work-with-project-boards/tracking-work-with-project-boards/adding-notes-to-a-project-board) (not Issues), except where an issue or feature is user reported.  With that said, Notes can be converted to Issues if in-progress and collaborative discussion is needed.
- Use the [Discussions](https://github.com/DaveSkender/Stock.Indicators/discussions) area for general ideation and unrelated questions.

## Developing

- Read this first: [A Step by Step Guide to Making Your First GitHub Contribution](https://codeburst.io/a-step-by-step-guide-to-making-your-first-github-contribution-5302260a2940).  I also have a discussion [on Forking](https://github.com/DaveSkender/Stock.Indicators/discussions/503) if you have questions.
- If you are adding a new indicator, the easiest way to do this is to copy the folder of an existing indicator and rename everything using the same naming conventions and taxonomy.  All new indicators should include unit and performance tests.
- Do not commingle multiple contributions.  Please keep changes small and separate.
- If you're just getting started, [install and setup](https://python.stockindicators.dev/guide/#installation-and-setup) language SDKs for Python and .NET.

## Development Environment Setup

### Windows Setup

1. Install .NET SDK (6.0 or newer):

    ```powershell
    winget install Microsoft.DotNet.SDK.6
    # Or download from https://dotnet.microsoft.com/download
    ```

2. Clone and setup:

    ```powershell
    git clone https://github.com/facioquo/stock-indicators-python.git
    cd stock-indicators-python
    pip install -r requirements.txt
    pip install -r requirements-test.txt
    ```

### macOS Setup

1. Install .NET SDK (6.0 or newer):

    ```bash
    brew install dotnet-sdk
    ```

2. Clone and setup:

    ```bash
    git clone https://github.com/facioquo/stock-indicators-python.git
    cd stock-indicators-python
    pip install -r requirements.txt
    pip install -r requirements-test.txt
    ```

## Testing

- We use [pytest](https://docs.pytest.org) for testing.
- Review the `tests` folder for examples of unit tests.  Just copy one of these.
- New indicators should be tested against manually calculated, proven, accurate results.  It is helpful to include your manual calculations spreadsheet in the appropriate indicator folder when [submitting changes](#submitting-changes).
- Historical Stock Quotes are automatically added as pytest fixtures.  The various `.csv` files in the `samples` folder are used in the unit tests.  See `tests/conftest.py` for their usage.  A `History.xlsx` Excel file is also included in the `samples` folder that contains the same information but separated by sheets.  Use this for your manual calculations to ensure that it is correct.  Do not commit changes to this Excel file.
- We expect all unit tests to execute successfully and all Errors and Warning resolved before you submit your code.
- Failed builds or unit testing will block acceptance of your Pull Request when submitting changes.

### Running Tests

```bash
# install core dependencies
pip install -r requirements.txt

# install test dependencies
pip install -r requirements-test.txt

# run standard unit tests
pytest
```

To run different types of tests, use the following commands:

- **Normal unit tests** (default):

  ```bash
  pytest
  ```

- **Non-standard `localization` tests**:

  ```bash
  pytest -m "localization"
  ```

- **Performance tests**:

  ```bash
  pytest -m "performance"
  ```

- **All tests** (not recommended):

  ```bash
  pytest -m ""
  ```

You can also use the `-svr A` arguments with pytest to get more detailed output:

- `-s`: Disable output capturing (show print statements)
- `-v`: Increase verbosity
- `-r A`: Show extra test summary info for all tests

```bash
pytest -svr A
```

### Performance benchmarking

Running the commands below in your console will show performance data.  You can find the latest results [here]({{site.baseurl}}/performance/).

```bash
# install dependencies
pip install -r requirements-test.txt

# run performance tests
pytest -m "performance"
```

## Documentation

This site uses [Jekyll](https://jekyllrb.com) construction with Front Matter.  The documentation site is in the `docs` folder.  Build the site locally to test that it works properly.
See [GitHub Pages documentation](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll) for initial setup instructions.

```bash
bundle install
bundle exec jekyll serve

# then open site on http://127.0.0.1:4000,
# or use `bundle exec jekyll serve -o -l` to auto-open, livereload
```

When adding or updating indicators:

- Add or update the indicator documentation `/docs/_indicators` files.
- Page image assets go in the `/docs/assets/` folder.

## Submitting changes

By submitting changes to this repo you are also acknowledging and agree to the terms in both the [Developer Certificate of Origin (DCO) 1.1](https://developercertificate.org) and the [Apache 2.0 license](https://opensource.org/licenses/Apache-2.0).  These are standard open-source terms and conditions.

When ready, submit a Pull Request with a clear list of what you've done (read more about [pull requests](http://help.github.com/pull-requests)).  Always write a clear log message for your commits. One-line messages are fine for most changes.

After a Pull Request is reviewed, accepted, and [squash] merged to `main`, we may batch changes before publishing a new package version to PyPI.  Please be patient with turnaround time.

## Code reviews and administration

If you want to contribute administratively, do code reviews, or provide general user support, we're also currently seeking a few core people to help.  Please [contact us](#contact-info) if interested.

## Standards and design guidelines

- [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
- [PEP 440 -- Version Identification and Dependency Specification](https://www.python.org/dev/peps/pep-0440/)
- [Semantic Version 2.0](https://semver.org)
- [Python Packaging User Guide](https://packaging.python.org/)

## Versioning

We use the `setuptools_scm` tool for [semantic versioning](https://semver.org).  It detects the version number from `git tag` in the [GitHub Actions build](https://github.com/facioquo/stock-indicators-python/deployments/pypi).

Type | Format | Description
------------ | ------ | -----------
Major | `x.-.-` | A significant deviation with major breaking changes.
Minor | `-.x.-` | A new feature, usually new non-breaking change, such as adding an indicator.  Minor breaking changes may occur here and are denoted in the [release notes](https://github.com/facioquo/stock-indicators-python/releases).
Patch | `-.-.x` | A small bug fix, chore, or documentation change.

After one of our repository administrators creates a `git tag` on the `main` branch, reflecting the new version number, the `PyPI` deployment workflow will start.  After the new package is published, they'll publicly post the [release record](https://github.com/facioquo/stock-indicators-python/releases) with [automatically generated notes](https://docs.github.com/en/repositories/releasing-projects-on-github/automatically-generated-release-notes) and other information.

## License

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

This repository uses a standard Apache 2.0 open-source license.  It enables open-source community development by protecting the project and contributors from certain legal risks while allowing the widest range of uses, including in closed source software.  Please review the [license](https://opensource.org/licenses/Apache-2.0) before using or contributing to the software.

## Contact info

[Start a new discussion, ask a question](https://github.com/DaveSkender/Stock.Indicators/discussions), or [submit an issue](https://python.stockindicators.dev/contributing/#reporting-bugs-and-feature-requests) if it is publicly relevant.  You can also direct message [@daveskender](https://twitter.com/messages/compose?recipient_id=27475431).

Thanks,
Dong-Geon Lee
Dave Skender
