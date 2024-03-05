import os
import requests.compat


class InstagramBasicDisplayAPI:
    def __init__(self, params):
        self.app_id = params.get("INSTAGRAM_APP_ID")
        self.app_secret = params.get("INSTAGRAM_APP_SECRET")
        self.redirect_uri = params.get("INSTAGRAM_APP_REDIRECT_URI")
        self.get_code = params.get("get_code", '')
        self.api_base_url = 'https://api.instagram.com/'
        self.authorization_url = None

    def set_authorization_url(self):
        variables = {
            "app_id": self.app_id,
            "redirect_uri": self.redirect_uri,
            "scope": "user_profile,user_media",
            "response_type": "code"
        }
        self.authorization_url = f"{self.api_base_url}oauth/authorize?{requests.compat.urlencode(variables)}"


params = {
    "INSTAGRAM_APP_ID": os.getenv("INSTAGRAM_APP_ID"),
    "INSTAGRAM_APP_SECRET": os.getenv("INSTAGRAM_APP_SECRET"),
    "INSTAGRAM_APP_REDIRECT_URI": os.getenv("INSTAGRAM_API_REDIRECT_URI"),
    "get_code": "code received from authorization"
}

api = InstagramBasicDisplayAPI(params)

print(api)
