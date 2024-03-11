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
        self.user_access_token = ""
        self.has_user_access_token = False
        self.user_id = ''

    def set_authorization_url(self):
        variables = {
            "app_id": self.app_id,
            "redirect_uri": self.redirect_uri,
            "scope": "user_profile,user_media",
            "response_type": "code"
        }
        self.authorization_url = f"{self.api_base_url}oauth/authorize?{requests.compat.urlencode(variables)}"

    def set_user_instagram_access_token(self, params):
        if 'access_token' in params:
            self.user_access_token = params['access_token']
            self.has_user_access_token = True
            self.user_id = params['user_id']
        elif self.get_code:
            user_access_token_response = self.get_user_access_token()
            self.user_access_token = user_access_token_response['access_token']
            self.has_user_access_token = True
            self.user_id = user_access_token_response['user_id']
            long_lived_access_tkon_response = self.get_long_lived_user_access_token()
            self.user_access_token = long_lived_access_tkon_response['access_token']
            self.user_access_token_expires = long_lived_access_tkon_response['expires_in']

    def get_user_access_token(self):
        endpoint_url = f"{self.api_base_url}oauth/access_token"
        data = {
            "client_id": self.app_id,
            "client_secret": self.app_secret,
            "grant_type": "authorization_code"
        }
        response = requests.post(endpoint_url, data=data)
        return response.json()

    def get_long_lived_user_access_token(self):
        pass



params = {
    "INSTAGRAM_APP_ID": os.getenv("INSTAGRAM_APP_ID"),
    "INSTAGRAM_APP_SECRET": os.getenv("INSTAGRAM_APP_SECRET"),
    "INSTAGRAM_APP_REDIRECT_URI": os.getenv("INSTAGRAM_API_REDIRECT_URI"),
    "get_code": "code received from authorization"
}

api = InstagramBasicDisplayAPI(params)

print(api)
api.set_authorization_url()