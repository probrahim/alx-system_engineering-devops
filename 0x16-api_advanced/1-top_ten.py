#!/usr/bin/python3

"""
the titles of the first 10
"""

from requests import get


def top_ten(subreddit):
    """
    function that queries the Reddit API """

    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    params = {'limit': 10}
    url_base = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    ml = get(url_base, headers=user_agent, params=params)
    total = ml.json()

    try:
        my_data = total.get('data').get('children')

        for i in my_data:
            print(i.get('data').get('title'))

    except Exception:
        print("None")
