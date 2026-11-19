#!/usr/bin/env python3

import csv
import os
import sys

from argparse import ArgumentParser

from github import Auth, Github, GithubException, GithubObject
from urllib3 import Retry


def starred_repos(user):
    """Return every repository the user has starred, across all pages, as one flat list."""
    return list(user.get_starred())


def config_retry(backoff_factor=1.0, total=8):
    """urllib3 will sleep for:
        {backoff factor} * (2 ** ({number of total retries} - 1))

    Caps the backoff at the longest sleep this schedule produces."""
    return Retry(
        total=total,
        backoff_factor=backoff_factor,
        backoff_max=backoff_factor * 2 ** (total - 1),
    )


def parse_args():
    parser = ArgumentParser(description="export a GitHub user's starred repositories to CSV")
    parser.add_argument("--user")
    parser.add_argument(
        "--auth-token",
        default=os.environ.get("GITHUB_TOKEN"),
        help="GitHub token (defaults to $GITHUB_TOKEN)",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    if not (args.auth_token or args.user):
        print("Please set `--user` to a valid GitHub user name.", file=sys.stderr)
        sys.exit(1)

    auth = Auth.Token(args.auth_token) if args.auth_token else None
    client = Github(auth=auth, per_page=100, retry=config_retry())
    sys.stdout.reconfigure(newline="")
    writer = csv.writer(sys.stdout)

    try:
        user = client.get_user(args.user or GithubObject.NotSet)
        repos = starred_repos(user)
    except GithubException as e:
        print(f"GitHub request failed ({e.status}): {e.data}", file=sys.stderr)
        if e.status == 403 and not args.auth_token:
            print("You may be rate limited; pass --auth-token or set GITHUB_TOKEN.", file=sys.stderr)
        sys.exit(1)

    writer.writerows((repo.html_url, repo.description) for repo in repos)


if __name__ == "__main__":
    main()
