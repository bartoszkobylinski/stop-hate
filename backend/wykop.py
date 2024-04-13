import requests


def get_wykop_user_info(username, api_key):
    url = f"https://a2.wykop.pl/Users/Profile/{username}/appkey/{api_key}"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to retrieve user information"}


def get_wykop_user_posts(username, api_key):
    url = ''
    response = requests.get(url)

    return response.json()
