#!/usr/bin/env python3
import tweepy
import sys
import time
import os

from dotenv import load_dotenv
load_dotenv()

API_KEY = os.environ.get("API_KEY") 
API_SECRET = os.environ.get("API_SECRET")

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ACCESS_SECRET = os.environ.get("ACCESS_SECRET") 


def main(args):
    screen_name = args[1]
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    try:
        for follower in tweepy.Cursor(api.followers, screen_name, count=200).items():
            sys.stdout.write(follower.screen_name)
            sys.stdout.write('\n')
    except tweepy.TweepError:
        print("tweepy.TweepError=")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main(sys.argv)
