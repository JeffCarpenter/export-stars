This script exports a GitHub user's starred repositories (URL & description) to a CSV file.

Setup:

    python -m pip install -r requirements.txt
    pip install -r requirements.txt

Usage:

NOTE1 Under Microsoft Windows may need to set:

    set PYTHONUTF8=1

NOTE2 Can use without a token BUT if there are a lot of stars need a token to avoid `github.GithubException.RateLimitExceededException`

    GH_USER=defunkt python3 export_stars/export_stars.py > stars.csv
    python export_stars/export_stars.py --user defunkt > stars.csv

Thanks to the authors of [PyGitHub](https://github.com/PyGithub/PyGithub) for the slick client library.
