from tweepy import OAuthHandler
from tweepy import API
import urllib.request
import os
import json

consumer_key = "XXXXXXXXXXX"
consumer_secret = "XXXXXXXXXXX"
access_token = "XXXXXXXXXXX"
access_token_secret = "XXXXXXXXXXX"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = API(auth)

with open('index.txt', 'r') as indexNmr:
    vari = int(indexNmr.read().strip())

json_input = open('[JSON file]')
data = json.load(json_input)
urllib.request.urlretrieve(data['tweets'][vari]['img'], 'image-temp.jpg')
filename = ('image-temp.jpg')

try:
    api.update_with_media(filename, status=data['tweets'][vari]['text'])
    os.remove(filename)
except:
    print('Error, baby.')

with open('index.txt', 'w') as indexNew:
    indexNew.write("%d" % (vari + 1))
