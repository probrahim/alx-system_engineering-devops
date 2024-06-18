#!/usr/bin/python3

"""requests HTTP """
from requests import get


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and returns the number of subscribers
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url_base = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    ml = get(url_base, headers=user_agent)
    total = ml.json()

    try:
        return total.get('data').get('subscribers')

    except Exception:
        return 0
