#!/usr/bin/python3
"""extend your Python script to export data in the CSV format"""
import csv
import requests
from sys import argv


if __name__ == '__main__':

    user_id = argv[1]

    response_user = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'.format(
                user_id))
    user = response_user.json()
    name = user.get('name')
    response_posts = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
                user_id))
    posts = response_posts.json()

    with open("{}".format(user_id) + ".csv", "w") as file:
        writer = csv.writer(file, dialect='unix')
        for dict_posts in posts:
            writer.writerow(
                    [user_id,
                        name,
                        dict_posts.get('completed'),
                        dict_posts.get('title')])
