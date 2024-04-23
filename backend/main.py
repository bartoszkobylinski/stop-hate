import requests
import json


class InstagramMediaFetcher:
    def __init__(self, access_token, user_id):
        self.access_token = access_token
        self.user_id = user_id
        self.base_url = f"https://graph.instagram.com/{user_id}/media"

    def get_user_media(self):
        url = f"{self.base_url}?fields=id,caption&access_token={self.access_token}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['data']
        else:
            return f"Error: {response.text}"

    def print_media(self):
        media = self.get_user_media()
        print(json.dumps(media, indent=1))


if __name__ == "__main__":
    access_token = "abosteuthue"
    user_id = "123"
    media_fetcher = InstagramMediaFetcher(access_token, user_id)
    media_fetcher.print_media()
