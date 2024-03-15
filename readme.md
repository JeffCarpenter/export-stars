This script exports a GitHub user's starred repositories (URL & description) to a CSV file.

Usage: `python export_stars.py --user=GH_USER --token=TOKEN > stars.csv`

To generate the token, go to Settings > Advanced Settings > Personal access tokens (classic). Limit its scope to `public_repo`.

Thanks to the authors of [PyGitHub](https://github.com/PyGithub/PyGithub) for the slick client library.
