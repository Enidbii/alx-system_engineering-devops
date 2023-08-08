#!/usr/bin/python3
""" recursive function that queries reddit api """
from requests import get



def recurse(subreddit, hot_list=[]):
    """
    queries reddit api
    returns list containing titles of artcles
    if none is found return none
    """
    apiUrl = "https://reddit.com/r/{}/hot.json".format(subreddit)
    userAgent = "Mozilla/5.0"

