# General imports.
from pymongo import MongoClient
from twython import Twython
from twython import TwythonStreamer
from configparser import ConfigParser
import tweepy
import config
from tweepy import OAuthHandler

try:
    import json
except ImportError:
    import simplejson as json

from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

ACCESS_TOKEN = config.access_token
ACCESS_SECRET = config.access_secret
CONSUMER_KEY = config.consumer_key
CONSUMER_SECRET = config.consumer_secret

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter Streaming API.
twitter_stream = TwitterStream(auth=oauth)

# Get the data.
iterator = twitter_stream.statuses.filter(track='mariners, seattlemariners', language='en')

tweet_count = 1000
for tweet in iterator:
    tweet_count -= 1
    print(json.dumps(tweet))

    if tweet_count <= 0:
        break
