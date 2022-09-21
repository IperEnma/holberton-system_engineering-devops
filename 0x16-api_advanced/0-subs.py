#!/usr/bin/python3
"""returns the number of subscribers"""
import requests

def number_of_subscribers(subreddit):
    """returns the number of subscribers"""

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/81.0',
        'From': 'enmanuelhernandez1843@gmail.com'  # This is another valid field
    }
    try:
        response = requests.get(url, headers=headers)
        return (response.json()['data']['subscribers'])
    except Exception:
        return 0
