# export-stars

Export a GitHub user's starred repositories to CSV. Each row contains the repository URL and description, in that order. The CSV has no header row.

## Install

From the repository root, use [uv](https://docs.astral.sh/uv/) with Python 3.14.

```sh
uv sync --locked
```

## Usage

View the available options with `uv run --locked export-stars --help`. The CLI takes `--user` for the GitHub username and `--github-token` for an optional token. It is designed to write CSV to standard output, so you can redirect it to a file.

```sh
uv run --locked export-stars --user octocat > stars.csv
```

**Known issue:** The current CLI exits before contacting GitHub because it reads `args.token` while the parser stores `args.github_token`. Until that is fixed, use the Python API to export public stars.

```sh
uv run --locked python - > stars.csv <<'PY'
import csv
import sys

from github import Github

from export_stars import starred_repos

user = Github().get_user("octocat")
writer = csv.writer(sys.stdout)
for repo in starred_repos(user):
    writer.writerow((repo.html_url, repo.description))
PY
```

Replace `octocat` with the GitHub username you want to export.

## Development

Run `uv build` to build the source distribution and wheel. See [Repository Guidelines](AGENTS.md) for contributor instructions.
