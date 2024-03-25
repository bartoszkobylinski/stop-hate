import requests
import json

access_token = "abosteuthue"
user_id = "123"
url = f"https://graph.instagram.com/{user_id}/media?fields=id,caption&access_token={access_token}"


def get_user_media(access_token, user_id, url):
    url = url
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['data']
    else:
        return f"Error: {response.text}"





media = get_user_media(access_token, user_id, url)

print(json.dumps(media, indent=1))
