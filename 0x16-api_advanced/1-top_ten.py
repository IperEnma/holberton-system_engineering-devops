#!/usr/bin/python3
"""returns top ten by subredditer"""
import requests


def top_ten(subreddit):
    """returns top ten bysubredditer"""

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

    headers = {
        'User-Agent':
        'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/81.0',
        'From': 'enmanuelhernandez1843@gmail.com'
    }
    response = requests.get(url, headers=headers)
    response_json = response.json()
    for idx in range(len(response_json['data']['children'])):
        print(response_json['data']['children'][idx]['data']['title'])
        if idx == 9:
            break
