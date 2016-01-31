from urllib import urlretrieve
from server import http_server
from twit import twitter_api, get_pics


#for url in get_pics():
#    urlretrieve(url, "_pics/tmp/%s" % url.rsplit('/',1)[1])

http_server.run(debug=True)

