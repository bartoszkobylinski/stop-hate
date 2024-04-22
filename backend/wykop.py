import requests

class WykopAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://a2.wykop.pl"

    def get_user_info(self, username):
        url = f"{self.base_url}/Users/Profile/{username}/appkey/{self.api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Failed to retrieve user information"}

    def get_user_posts(self, username):
        url = f"{self.base_url}/Entries/Index/{username}/appkey/{self.api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Failed to retrieve user posts"}


