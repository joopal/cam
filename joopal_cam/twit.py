from time import sleep
from os import environ
import dotenv
import settings
import twitter


twitter_api = twitter.Api(consumer_key=environ.get("TWITTER_CONSUMER_KEY"),
        consumer_secret=environ.get("TWITTER_CONSUMER_SECRET"),
        access_token_key=environ.get("TWITTER_ACCESS_KEY"),
        access_token_secret=environ.get("TWITTER_ACCESS_SECRET"))


def get_pics():
    while True:
        last_id = environ.get("TWITTER_LAST_MEDIA_ID")
        results = twitter_api.GetSearch(term="#selfie", since_id=last_id, result_type="popular")
        results.reverse()
        for r in results:
            last_id = r.id
            for m in r.media:
                url = m["media_url_https"]
                print(url)
                sleep(4)
                yield url
            settings.write_config("TWITTER_LAST_MEDIA_ID", r.id)

