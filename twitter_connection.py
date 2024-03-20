import os
import tweepy


api_key = os.getenv("API_KEy")
api_secret = os.getenv("API_SECRET_KEY")
access_token = os.getenv("ACCeSS_TOKEN")
access_token_secret = os.getenv("ACCES_TOKEN_SECRET")

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

try:
    api.verif_cedentials()
    print("auth ok")
except:
    print("something went wongi")
