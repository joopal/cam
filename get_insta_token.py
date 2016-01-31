from instagram.client import InstagramAPI
import sys
from os import environ
import joopal_cam


if len(sys.argv) > 1 and sys.argv[1] == 'local':
    try:
        from test_settings import *
        InstagramAPI.host               = test_host
        InstagramAPI.base_path          = test_base_path
        InstagramAPI.access_token_field = "access_token"
        InstagramAPI.authorize_url      = test_authorize_url
        InstagramAPI.access_token_url   = test_access_token_url
        InstagramAPI.protocol           = test_protocol
    except Exception:
        pass


# Fix Python 2.x.
try:
    import __builtin__
    input = getattr(__builtin__, 'raw_input')
except (ImportError, AttributeError):
    pass


client_id     = environ.get("INSTA_CLIENT_ID")
client_secret = environ.get("INSTA_CLIENT_SECRET")

raw_scope     = input("Requested scope (separated by spaces, blank for just basic read): ").strip()
scope = raw_scope.split(' ')

# For basic, API seems to need to be set explicitly
if not scope or scope == [""]:
    scope = ["basic"]

print(environ.get("INSTA_REDIRECT_URI"))
api = InstagramAPI(
        client_id=environ.get("INSTA_CLIENT_ID"),
        client_secret=environ.get("INSTA_CLIENT_SECRET"),
        redirect_uri=environ.get("INSTA_REDIRECT_URI"))

redirect_uri = api.get_authorize_login_url(scope = scope)

print("Visit this page and authorize access in your browser: ")
print(redirect_uri)

code = str(input("Paste in code in query string after redirect: ").strip())

access_token = api.exchange_code_for_access_token(code)
print("access token: ")
print(access_token[1])
print(access_token[0])

