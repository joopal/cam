from os import environ
import twitter


api = twitter.Api(consumer_key=environ.get("TWITTER_CONSUMER_KEY"),
        consumer_secret=environ.get("TWITTER_CONSUMER_SECRET"),
        access_token_key=environ.get("TWITTER_ACCESS_KEY"),
        access_token_secret=environ.get("TWITTER_ACCESS_SECRET"))
