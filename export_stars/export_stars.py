#!env python

import sys
import csv

from math import ceil
from argparse import ArgumentParser

from github import Github
from github.GithubException import RateLimitExceededException


def starred_repos(user):
    starred = user.get_starred()
    total_pages = ceil(starred.totalCount / 30)

    for page_num in range(0, total_pages):
        for repo in starred.get_page(page_num):
            yield repo


def parse_args():
    parser = ArgumentParser(description="export a GitHub user's starred repositorys to CSV")
    parser.add_argument("--user")
    parser.add_argument("--github-token")
    return parser.parse_args()


def main():
    args = parse_args()
    if not args.user:
        print("Please set `--user` to a valid GitHub user name.", file=sys.stderr)
        exit(1)

    gh = Github(args.token) if args.token else Github()
    user = gh.get_user(args.user)

    writer = csv.writer(sys.stdout)

    for repo in starred_repos(user):
        writer.writerow((repo.html_url, repo.description))


if __name__ == "__main__":
    main()
