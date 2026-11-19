# export-stars

Export a GitHub user's starred repositories to CSV. Each row contains the repository URL and description, in that order. The CSV has no header row.

## Install

From the repository root, use [uv](https://docs.astral.sh/uv/) with Python 3.14.

```sh
uv sync --locked
```

## Usage

View the available options with `uv run --locked export-stars --help`. The CLI takes `--user` for the GitHub username and `--auth-token` for an optional token, which defaults to the `GITHUB_TOKEN` environment variable. With a token and no `--user`, it exports the authenticated user's stars. It writes CSV to standard output and errors to standard error, so you can redirect it to a file.

```sh
uv run --locked export-stars --user octocat > stars.csv
GITHUB_TOKEN=... uv run --locked export-stars > my-stars.csv
```

Unauthenticated requests are limited to 60 per hour, about 6,000 stars at 100 per page. All pages are fetched before any CSV is written, so if GitHub refuses a request, the command exits with status 1 and writes no rows.

Python callers can use `export_stars.starred_repos(user)`, which returns a flat list of every repository starred by a PyGithub user object.

## Development

Run `uv build` to build the source distribution and wheel. See [Repository Guidelines](AGENTS.md) for contributor instructions.
