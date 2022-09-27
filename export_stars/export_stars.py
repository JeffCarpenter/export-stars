#!env python

import os
import sys
import csv

from math import ceil
from github import Github


def starred_repos(user):
    starred = user.get_starred()
    total_pages = ceil(starred.totalCount / 30)

    for page_num in range(0, total_pages):
        for repo in starred.get_page(page_num):
            yield repo


def main():
    user_name = os.environ.get("GH_USER", None)
    if not user_name:
        print("Please set environmental variable 'GH_USER' to a valid GitHub user name.", file=sys.stderr)
        exit(1)
    token = os.environ.get("GITHUB_TOKEN")

    gh = Github(token) if token else Github()
    user = gh.get_user(user_name)

    writer = csv.writer(sys.stdout)
    for repo in starred_repos(user):
        writer.writerow((repo.html_url, repo.description))


if __name__ == "__main__":
    main()
