#!/usr/bin/python3
"""given employee ID"""
import requests

response_user = requests.get('https://jsonplaceholder.typicode.com/users/2')
user = response_user.json()
user_id = user['id']
response_posts = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
            user_id))
posts = response_posts.json()
tasks = len(posts)
completed = 0
for _dict in posts:
    if _dict['completed'] is True:
        completed += 1
print("Employee {} is done with tasks({}/{}):".format(
    user['name'],
    completed,
    tasks))
for _dict in posts:
    if _dict['completed'] is True:
        print("     {}".format(_dict['title']))
