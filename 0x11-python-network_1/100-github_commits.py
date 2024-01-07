#!/usr/bin/python3
"""
Script that lists 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails” using GitHub API.
"""


import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Usage: {} <repository name> <owner name>".format(sys.argv[0]))

    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    # GitHub API endpoint for listing commits
    url = "https://api.github.com/repos/{}/{}/commits".format(owner_name, repo_name)

    # Send GET request to GitHub API
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        commits = response.json()[:10]  # Get the first 10 commits

        # Print commits in the specified format
        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print("{}: {}".format(sha, author_name))
    else:
        print("Error: Unable to fetch commits. Status Code:", response.status_code)
