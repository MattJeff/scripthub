import requests

BUBBLE_API_URL = 'https://votre-app.bubbleapps.io/api/1.1/obj/'

def add_creator(user_id, username):
    url = f"{BUBBLE_API_URL}creator"
    data = {
        'user_id': user_id,
        'username': username
    }
    response = requests.post(url, json=data)
    return response.json()

def add_video(creator_id, url, text, likes, views, comments):
    url = f"{BUBBLE_API_URL}video"
    data = {
        'creator_id': creator_id,
        'url': url,
        'text': text,
        'likes': likes,
        'views': views,
        'comments': comments
    }
    response = requests.post(url, json=data)
    return response.json()
