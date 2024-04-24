import requests
import json


class InstagramMediaFetcher:
    def __init__(self, access_token, user_id):
        self.access_token = access_token
        self.user_id = user_id
        self.base_url = f"https://graph.instagram.com/{user_id}/media"

    def get_user_media(self):
        url = f"{self.base_url}?fields=id,caption&access_token={self.access_token}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            try:
                return response.json()['data']
            except KeyError:
                return f"Error: Malformed JSON response, missing expected 'data' key."
            except json.JSONDecodeError:
                return f"Error: Failed to parse JSON from response."
        except requests.exceptions.HTTPError as e:
            return f"Error: {e.response.status_code} - {e.response.text}"
        except requests.exceptions.RequestException as e:
            return f"Error: Network or request error - {e}"

    def print_media(self):
        media = self.get_user_media()
        if isinstance(media, list):
            print(json.dumps(media, indent=1))
        else:
            print(media)


if __name__ == "__main__":
    access_token = "abosteuthue"
    user_id = "123"
    media_fetcher = InstagramMediaFetcher(access_token, user_id)
    media_fetcher.print_media()
