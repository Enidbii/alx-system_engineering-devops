#!/usr/bin/python3
""" Queries Reddit API and prints titles of first 10 hotspost """


import requests


def top_ten(subreddit):
    """ top ten subreddit titles hotspots """
    apiUrl = "https://reddit.com/r/{}/hot.json".format(subreddit)
    userAgent = "Mozilla/5.0"
    limits = 10

    response = requests.get(apiUrl, headers={"user-agent": userAgent},
                            params={"limit": limits})
    if not response:
        print('None')
        return
    response = response.json()
    val_ret = response['data']['children']
    for dat in val_ret:
        print(obj['data']['title'])
    return
