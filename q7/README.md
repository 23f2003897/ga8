# Question 7: Pre-commit Hooks & CI Gate (Ruff)

## Objective
Implement a multi-layered code quality enforcement system using `ruff`. This ensures that all Python code is automatically linted and formatted both locally (before committing) and in the cloud (during a Pull Request).

## Implementation Details

### 1. Local Pre-commit Hook
- **Tool:** `pre-commit`
- **Linter/Formatter:** `ruff` (v0.4.4)
- **Logic:** Whenever a `git commit` is attempted, the system runs Ruff. If violations are found (like unused imports or bad spacing), Ruff fixes them automatically and blocks the commit until the fixes are staged.

### 2. CI Gate (GitHub Actions)
- **Workflow:** `.github/workflows/ruff-ci.yml`
- **Trigger:** `on: [pull_request]`
- **Validation:** Ensures that any code being merged into `main` satisfies the project's style and quality requirements. If the check fails, the Pull Request cannot be merged (Red X).

## Final Submission Data
- **Ruff Version:** 0.4.4
- **Successful CI Run:** [https://github.com/23f2003897/ga8/actions/runs/25131657998]

## Tech Stack
- **Ruff:** Rust-based Python linter.
- **GitHub Actions:** CI/CD automation.
- **YAML:** Configuration for hooks and workflows.
