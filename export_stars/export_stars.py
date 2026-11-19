#!env python

import sys
import csv

from math import ceil
from argparse import ArgumentParser
from functools import partial

from github import Auth, Github, GithubObject
from urllib3 import Retry


def starred_repos(user):
    starred = user.get_starred()
    total_pages = ceil(starred.totalCount / 30)

    for page_num in range(0, total_pages):
        for repo in starred.get_page(page_num):
            yield repo


def config_retry(backoff_factor=1.0, total=8):
    """urllib3 will sleep for:
        {backoff factor} * (2 ** ({number of total retries} - 1))

    Recalculates and Overrides Retry.DEFAULT_BACKOFF_MAX"""
    Retry.DEFAULT_BACKOFF_MAX = backoff_factor * 2 ** (total - 1)
    return Retry(total=total, backoff_factor=backoff_factor)


def parse_args():
    parser = ArgumentParser(description="export a GitHub user's starred repositorys to CSV")
    parser.add_argument("--user")
    parser.add_argument("--auth-token")
    return parser.parse_args()


def main():
    args = parse_args()
        
    gh = partial(Github, retry=config_retry())
    if args.auth_token:
        client = gh(auth=Auth.Token(args.auth_token))
        user = client.get_user(args.user or GithubObject.NotSet)
    elif args.user:
        client = gh()
        user = client.get_user(args.user)
    else:
        print("Please set `--user` to a valid GitHub user name.", file=sys.stderr)
        exit(1)

    writer = csv.writer(sys.stdout)

    for repo in starred_repos(user):
        writer.writerow((repo.html_url, repo.description))


if __name__ == "__main__":
    main()
