#!/usr/bin/python3

# requetes HTTP effectuer
from requests import get



def number_of_subscribers(subreddit):
    """ cette fonction prends un param pour obtenir les nombres d'abonnes"""


    if subreddit is None:
        return 0
    if not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url_base = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    mixte  = get(url_base, headers=user_agent)
    total = mixte,json()


    try:
        return total.get('data').get('subscribers')
    except Exception:
        return 0
