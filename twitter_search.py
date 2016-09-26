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

# Initiate the connection to Twitter REST API.
twitter = Twitter(auth=oauth)

tweets = 0
MAX_ATTEMPTS = 20
COUNT_OF_TWEETS_TO_BE_FETCHED = 1000
search_query = '#redsox since:2016-08-16 until:2016-08-17'
#search_query = '#yankees since:2016-08-16 until:2016-08-17'

for i in range(0,MAX_ATTEMPTS):

    if(COUNT_OF_TWEETS_TO_BE_FETCHED <= tweets):
        break # We got 1000 tweets.

    # Query Twitter.
    if(0 == i):
        results = twitter.search.tweets(q=search_query, lang='en', result_type='recent', count='100')
    else:
        results = twitter.search.tweets(q=search_query, lang='en', result_type='recent', count='100', include_entities='true', max_id=next_max_id)

    # Save tweets.
    for result in results['statuses']:
        print(json.dumps(result))
        tweets+=1

    # Get next max_id.
    try:
        next_results_url_params = results['search_metadata']['next_results']
        next_max_id = next_results_url_params.split('max_id=')[1].split('&')[0]
    except:
        break
