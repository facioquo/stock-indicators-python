# Developer Experience

This is a guide for setting up your development environment for the first time. It will walk you through the steps to install the necessary tools and dependencies to get started with development on this project.

## Prerequisites

Before you begin, make sure you have the following installed on your machine:

### Software

- [Git](https://git-scm.com/downloads)
- [Node.js](https://nodejs.org/en/download/)
- [npm](https://www.npmjs.com/get-npm)
- [Docker](https://docs.docker.com/get-docker/)
- [Python](https://www.python.org/downloads/)

### Tools

- [Docker Desktop](https://www.docker.com/products/docker-desktop)
- [Visual Studio Code](https://code.visualstudio.com/download)
  - see [extensions.json](.vscode/extensions.json) for recommended extensions

## Dev container

This project includes a [devcontainer](https://code.visualstudio.com/docs/remote/containers) configuration that allows you to develop in a containerized environment. This ensures that all developers are using the same development environment, regardless of their host machine.

To use the devcontainer, follow these steps:

1. Install the [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension for Visual Studio Code.
2. Open the project in Visual Studio Code.
3. Click on the green "><" icon in the bottom left corner of the window.
4. Select "Reopen in Container".

Visual Studio Code will now build the devcontainer and open a new window with the project running inside the container.

## Testing GitHub Actions locally

This project uses GitHub Actions for CI/CD. You can test the GitHub Actions workflows locally using [act](https://github.com/nektos/act). Since you're using the devcontainer, `act` is already installed and ready to use.

### VS Code Integration

Install the [GitHub Actions Local](https://marketplace.visualstudio.com/items?itemName=SanjulaGanepola.github-local-actions) extension to run workflows directly from VS Code:

- Open the Command Palette (Ctrl+Shift+P)
- Search for "Run GitHub Actions Workflow"
- Select the workflow you want to run

### CLI Usage

Basic commands:

```bash
# List all available workflows
act -l

# Run all workflows
act

# Run a specific workflow
act push
act pull_request

# Run a specific job in a workflow
act -j build

# Dry run (shows what would happen)
act -n

# Run with different event types
act workflow_dispatch
act release
```

Advanced usage:

```bash
# Run with specific event payload
act pull_request -e event.json

# Use custom secrets
act --secret-file my.secrets

# Verbose output for debugging
act -v

# Run workflow from a specific file
act -W .github/workflows/specific.yml
```

### Excluding Workflows

You can prevent specific workflows or jobs from running using several methods:

```bash
# Exclude specific workflows using -W with ! prefix
act -W '!.github/workflows/deploy.yml'

# Run only specific workflows (excludes others)
act -W '.github/workflows/test.yml' -W '.github/workflows/lint.yml'

# Exclude specific jobs using --exclude
act --exclude build-prod

# Skip certain event types
act -e pull_request --exclude-events "push,release"
```

A `.actrc` file in your project root can permanently exclude workflows:

```plaintext
# .actrc
--exclude-events "deployment,deployment_status"
-W '!.github/workflows/production.yml'
```

### Common Exclusion Patterns

- Production deployments: `*deploy*.yml`, `*prod*.yml`
- External service integrations: `*release*.yml`, `*publish*.yml`
- Resource-intensive workflows: Consider excluding with `--exclude` flag

### Configuring Permanent Exclusions

The `.actrc` file can be placed in three locations (in order of precedence):

1. Project directory: `<project-root>/.actrc`
2. Home directory: `~/.actrc`
3. XDG config directory: `~/.config/act/actrc`

For detailed documentation about `.actrc` configuration, see:

- [Act CLI configuration](https://github.com/nektos/act#configuration)
- [Act RC file format](https://github.com/nektos/act/blob/master/cmd/root.go#L113-L127)
- [Configuration examples](https://github.com/nektos/act/discussions/1816)

Example `.actrc` for excluding deployment workflows:

```plaintext
# Exclude all deployment-related workflows
-W '!.github/workflows/*deploy*.yml'
-W '!.github/workflows/*prod*.yml'
-W '!.github/workflows/release*.yml'

# Exclude deployment-related events
--exclude-events "deployment,deployment_status,release,workflow_dispatch"

# Exclude specific jobs
--exclude "deploy-*"
--exclude "*-prod"
--exclude "publish-*"
```

Place this file in your preferred location based on whether you want:

- Project-specific exclusions: use `<project-root>/.actrc`
- Global exclusions: use `~/.actrc`
- System-wide exclusions: use `~/.config/act/actrc`

### Common Arguments

| Argument | Description | Example |
|----------|-------------|---------|
| `-l` | List workflows | Shows available workflow files |
| `-n` | Dry run | Displays steps without execution |
| `-v` | Verbose output | Shows detailed execution logs |
| `-j` | Specify job | `-j build` runs only the 'build' job |
| `-W` | Workflow file | `-W .github/workflows/test.yml` |
| `--secret-file` | Load secrets | `--secret-file my.secrets` |
| `-e` | Event payload | `-e event.json` provides event data |

### Best Practices

1. Start with dry runs (`-n`) to verify workflow configuration
2. Use `-l` to confirm available workflows
3. Test specific jobs before running entire workflows
4. Keep secrets in a `.secrets` file (gitignored)

### Common Pitfalls

- Avoid running workflows that interact with production resources
- Don't commit secret files to version control
- Be cautious with workflows that modify repositories
- Remember that some GitHub-specific features may not work locally

For more information on `act`, see the [official documentation](https://github.com/nektos/act#readme).
