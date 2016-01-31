from os import environ
from flask import Flask, request
from instagram.client import InstagramAPI
from insta import insta_api


http_server = Flask("joopal_cam")


@http_server.route("/")
def root():
    return "root"

@http_server.route("/oauth")
def oauth():
    access_token = request.args["code"]
    print(access_token)
    return "oauth"

@http_server.route("/search")
def search():
    tag_search = ["selfie"]
    for tag in tag_search:
        print("tag name: %s" % tag)
        selfies, _next = insta_api.tag_recent_media(tag_name=tag)
        for selfie in selfies:
            print("selfie: %s" % selfie)
    #return "<br />".join([str(s.media_count) for s in selfies])
    return "search"

@http_server.route("/user/<username>")
def user(username):
    media, _next = insta_api.user_recent_media()
    ids_and_urls = [(m.id, m.images["standard_resolution"].url) for m in media]
    return "<br />".join(
            ["<a href=\"%s\">%s</a>" % (urls, _id) for _id, urls in ids_and_urls])

