#!/usr/bin/env python
# encoding: utf-8

import tweepy
import json
import time

#Twitter API credentials
consumer_key = "Enter Consumer Key"
consumer_secret = "Enter Consumer Secret"
access_key = "Enter Access Key"
access_secret = "Enter Access Secret"

latitude = 48.857732    # geographical centre of search
longitude = 2.350943    # geographical centre of search
max_range = 75            # search range in kilometres

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

#Put your search term

searchquery = 'python' #Enter words to be searched

users =tweepy.Cursor(api.search,q=searchquery, geocode = "Enter geocode if any specific",lang="Enter language of tweet to").items()
count = 0
errorCount=0

file = open('Filename.json', 'w')

while True:
    try:
        user = next(users)
    except tweepy.TweepError:
        print("sleeping....")   
        time.sleep(60*10)
        user = next(users)
    except StopIteration:
        break
    try:
        print("Writing to JSON tweet number:"+str(count))
        count += 1
        json.dump(user._json,file,sort_keys = True,indent = 4)

    except UnicodeEncodeError:
        errorCount += 1
        print("UnicodeEncodeError,errorCount ="+str(errorCount))

print("completed, errorCount ="+str(errorCount)+" total tweets="+str(count))