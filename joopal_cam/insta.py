from os import environ
from instagram.client import InstagramAPI


insta_api = InstagramAPI(
        client_id=environ.get("INSTA_CLIENT_ID"),
        client_secret=environ.get("INSTA_CLIENT_SECRET"),
        access_token=environ.get("INSTA_ACCESS_TOKEN"),
        redirect_uri=environ.get("INSTA_REDIRECT_URI"))

