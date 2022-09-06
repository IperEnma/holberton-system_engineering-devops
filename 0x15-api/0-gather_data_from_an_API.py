#!/usr/bin/python3
"""given employee ID and tittles"""

import requests
from sys import argv

if __name__ == '__main__':
    """principal function"""

    response_user = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'.format(
                argv[1]))
    user = response_user.json()
    user_id = user.get('id')
    response_posts = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
                user_id))
    posts = response_posts.json()
    tasks = len(posts)
    completed = 0
    for _dict in posts:
        if _dict.get('completed') is True:
            completed += 1
    print("Employee {} is done with tasks({}/{}):".format(
        user['name'],
        completed,
        tasks))
    for _dict in posts:
        if _dict.get('completed') is True:
            print("\t {}".format(_dict['title']))
