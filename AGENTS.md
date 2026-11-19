# Repository Guidelines

## Project Structure

`export_stars/export_stars.py` implements the CLI, GitHub pagination, retry configuration, and CSV output. `export_stars/__init__.py` exposes `starred_repos(user)` for Python callers. The flat package layout, dependencies, and `export-stars` entry point are defined in `pyproject.toml`. Keep `uv.lock` in sync with dependency changes. The package uses `README.md` for its long description.

## Build and Development Commands

Use uv with Python 3.14, as pinned in `.python-version`.

- `uv sync --locked` installs the project and its locked dependencies.
- `uv lock --check` checks whether the lockfile matches the project metadata.
- `uv build` builds the source distribution and wheel.
- `uv run --locked export-stars --help` checks that the installed CLI starts and lists its options.

The export path currently raises `AttributeError` because the parser stores `--github-token` as `github_token` and `main()` reads `args.token`.

## Coding Style

Use four spaces for Python indentation and `snake_case` for functions and variables. Follow the surrounding code for imports and naming. Preserve the public `starred_repos(user)` iterator when changing pagination. Write CSV rows to standard output and diagnostics to standard error so shell redirection produces a usable CSV file. Keep GitHub credentials out of tracked files and examples.

## Testing

The repository currently has no automated test suite, coverage target, formatter, or linter configuration. For CLI changes, run the help command and exercise the changed arguments. For pagination or CSV changes, use stub GitHub responses to check empty results, multiple pages, and descriptions containing commas or quotes.

## Commits and Pull Requests

Use short, action-oriented commit subjects, following recent examples such as “Configure uv packaging for the existing flat layout.” In pull requests, summarize the change and its effect on callers, list the checks you ran, and link any related issue.
