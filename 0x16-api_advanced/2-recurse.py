#!/usr/bin/python3
"""recursive function that queries"""
import requests


def recurse(subreddit, hot_list=[]):
    """recursive function that queries"""

    if type(subreddit) is not list:
        url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    else:
        url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(subreddit[0], subreddit[1])

    headers = {
            'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/81.0',
            'From': 'enmanuelhernandez1843@gmail.com'
            }
    try:
        response = requests.get(url, headers=headers)
        response_json = response.json()
        for idx in range(len(response_json['data']['children'])):
            hot_list.append(response_json['data']['children'][idx]['data']['title'])
        if (response_json['data']['after']) is None:
            return hot_list
        else:
            subreddit = response_json['data']['children'][0]['data']['subreddit']
            after = response_json['data']['after']
            return recurse([subreddit, after], hot_list)
    except Exception as e:
        print(e)
