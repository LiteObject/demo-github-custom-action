# Demo Github Custom Action
>Actions are individual tasks that you can combine to create jobs and customize your workflow. You can create your own actions, or use and customize actions shared by the GitHub community.

>You can create actions by writing custom code that interacts with your repository in any way you'd like, including integrating with GitHub's APIs and any publicly available third-party API. For example, an action can publish npm modules, send SMS alerts when urgent issues are created, or deploy production-ready code.

## Types of actions

| Type | Linux | macOS | Windows |
|-|-|-|-|
| Docker container actions | X |   |   |
| JavaScript actions | X | X | X |
| Composite Actions | X | X | X |

### Docker container actions
Docker containers package the environment with the GitHub Actions code. This creates a more consistent and reliable unit of work because the consumer of the action does not need to worry about the tools or dependencies.

### JavaScript actions
JavaScript actions can run directly on a runner machine, and separate the action code from the environment used to run the code. Using a JavaScript action simplifies the action code and **executes faster** than a Docker container action.

### Composite Actions
A composite action allows us to combine multiple workflow steps within one action.

---
## Links
- [GitHub: Creating actions](https://docs.github.com/en/actions/creating-actions)
- [Creating a Docker container action](https://docs.github.com/en/actions/creating-actions/creating-a-docker-container-action)