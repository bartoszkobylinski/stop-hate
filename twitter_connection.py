import os
import tweepy


class TweeterCLient:

    def __init__(self):
        api_key = os.getenv("API_KEy")
        api_secret = os.getenv("API_SECRET_KEY")
        access_token = os.getenv("ACCeSS_TOKEN")
        access_token_secret = os.getenv("ACCES_TOKEN_SECRET")

        auth = tweepy.OAuthHandler(api_key, api_secret)
        auth.set_access_token(access_token, access_token_secret)

        self.api = tweepy.API(auth)

        try:
            self.api.verify_cedentials()
            print("auth ok")
        except:
            print("something went wongi")

    def get_user_info(self, user_id):
        try:
            user = self.api.get_user(user_id=user_id)
            return {
                "name": user.name,
                "description": user.description,
                "followers_count": user.followers_count
            }
        except Exception as error:
            return {"error": str(error)}

