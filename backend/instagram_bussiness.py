import requests

def get_user_info_and_posts(username, endpoint, access_token):
    params = {
        'fields': f'business_discovery.username({username}){{username,website,name,ig_id,id,profile_picture_url,biography,follows_count,followers_count,media_count,media{{id,caption,like_count,comments_count,timestamp,username,media_product_type,media_type,owner,permalink,media_url,children{{media_url}}}}}}',
        'access_token': access_token
    }

    response = requests.get(endpoint, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retreve data: {response.status_code}")

