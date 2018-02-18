from tweepy import OAuthHandler
from tweepy import API
import json
from time import sleep
import urllib.request
import os

consumer_key = "XXXXXXXXXXXXXXX"
consumer_secret = "XXXXXXXXXXXXXXX"
access_token = "XXXXXXXXXXXXXXX"
access_token_secret = "XXXXXXXXXXXXXXX"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = API(auth)

json_input = open('[json file]')
data = json.load(json_input)

for x in data['tweets']:
    urllib.request.urlretrieve(x['img'], 'image-temp.jpg')
    filename = ('image-temp.jpg')
    api.update_with_media(filename, status=x['text'])
    os.remove(filename)
    sleep(1800)
