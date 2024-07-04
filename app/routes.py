from flask import Blueprint, request, jsonify
from .scraper import get_instagram_profile_info, download_instagram_video, get_video_info, process_video
from .whisper_transcriber import transcrire_video
import requests
from .bubble_api import add_creator, add_video

main = Blueprint('main', __name__)

from flask import Blueprint, request, jsonify
from .scraper import get_instagram_profile_info, download_instagram_video, process_video
from .whisper_transcriber import transcrire_video
import requests
from .bubble_api import add_creator, add_video

main = Blueprint('main', __name__)

@main.route('/add_creator', methods=['POST'])
def add_creator_route():
    data = request.json
    username = data.get('username')
    user_id = data.get('user_id')

    if not username or not user_id:
        return jsonify({'error': 'Missing username or user_id'}), 400

    response = add_creator(user_id, username)
    if response.get('status') == 'success':
        return jsonify({'message': 'Creator added successfully'}), 201
    else:
        return jsonify({'error': response.get('message')}), 400

@main.route('/track_creator', methods=['POST'])
def track_creator():
    data = request.json
    username = data.get('username')
    num_videos = data.get('num_videos')

    if not username or not num_videos:
        return jsonify({'error': 'Missing username or num_videos'}), 400

    num_videos = int(num_videos)
    video_file_paths, status_code = get_instagram_profile_info(username, num_videos)

    if status_code == 200:
        videos_info = []
        # Assumer que vous avez une méthode pour obtenir creator_id depuis Bubble
        creator_id = ...  # Obtenez le creator_id depuis Bubble
        for video_file_path, post in video_file_paths:
            script = process_video(video_file_path)  # Utilisation de la fonction pour traiter et uploader la vidéo
            video_info = get_video_info(post)
            response = add_video(creator_id, post.url, script, post.likes, post.video_view_count, post.comments)
            if response.get('status') == 'success':
                videos_info.append(video_info)
        return jsonify({'videos': videos_info}), 200
    else:
        return jsonify({'error': video_file_paths}), status_code

@main.route('/track_videos', methods=['POST'])
def track_videos():
    data = request.json
    video_urls = data.get('video_urls')

    if not video_urls:
        return jsonify({'error': 'Missing video URLs'}), 400

    video_file_paths = []
    for url in video_urls:
        result, status_code = download_instagram_video(url)
        if status_code == 200:
            video_file_paths.append(result)
        else:
            return jsonify({'error': result}), status_code

    if video_file_paths:
        videos_info = []
        # Assumer que vous avez une méthode pour obtenir creator_id depuis Bubble
        creator_id = ...  # Obtenez le creator_id depuis Bubble
        for video_file_path, post in video_file_paths:
            script = process_video(video_file_path)  # Utilisation de la fonction pour traiter et uploader la vidéo
            video_info = get_video_info(post)
            response = add_video(creator_id, post.url, script, post.likes, post.video_view_count, post.comments)
            if response.get('status') == 'success':
                videos_info.append(video_info)
        return jsonify({'videos': videos_info}), 200
    else:
        return jsonify({'error': 'No valid videos provided.'}), 400

def get_creator_id(username):
    url = f"https://votre-app.bubbleapps.io/api/1.1/obj/creator?username={username}"
    response = requests.get(url)
    data = response.json()
    if data and 'status' in data and data['status'] == 'success':
        return data['response']['results'][0]['_id']
    return None

def get_creator_id_from_url(url):
    # Logique pour obtenir le creator_id à partir de l'URL de la vidéo
    username = extract_username_from_url(url)
    return get_creator_id(username)

def extract_username_from_url(url):
    # Logique pour extraire le nom d'utilisateur à partir de l'URL de la vidéo
    pass
