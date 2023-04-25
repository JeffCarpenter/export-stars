# Export stars from GitHub user

This script exports a GitHub user's starred repositories (URL & description) to a CSV file.

## Prepare environment

Install requirements `python3 -m pip install -r requirements.txt`

Usage: `GH_TOKEN=xxxxxx python3 export_stars.py --user githubusername > stars.csv`

Thanks to the authors of [PyGitHub](https://github.com/PyGithub/PyGithub) for the slick client library.
