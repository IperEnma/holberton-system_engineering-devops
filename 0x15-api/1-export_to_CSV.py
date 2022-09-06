#!/usr/bin/python3
"""extend your Python script to export data in the CSV format"""
import csv
import requests
from sys import argv


if __name__ == '__main__':

    user_id = argv[1]

    response_user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(user_id))
    user = response_user.json()
    name = user.get('name')
    response_posts = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.format(user_id))
    posts = response_posts.json()

    for dict_posts in posts:
        from_csv = []
        from_csv.append(str(user_id))
        from_csv.append(str(name))
        from_csv.append(str(dict_posts.get('completed')))
        from_csv.append(str(dict_posts.get('title')))
        with open("{}".format(user_id) + ".csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow(from_csv)
