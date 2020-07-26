import tweepy 

from tweepy import OAuthHandler 

## Authorisation file in order to access API methods.

consumer_key = ''
consumer_secret = ''

access_token = ''
access_secret = ''

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)