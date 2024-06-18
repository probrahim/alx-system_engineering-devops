#!/usr/bin/python3
"""
number of subscribers for a given subreddit
"""

from requests import get
import sys


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    """

    if subreddit is None:
        return 0

    if not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url_base = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url_base, headers=user_agent, allow_redirects=False)

    if response.status_code != 200:
        return 0

    try:
        results = response.json()
        return results.get('data', {}).get('subscribers', 0)
    except ValueError:
        return 0


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
