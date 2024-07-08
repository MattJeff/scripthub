from flask import Blueprint, request, jsonify
from .scraper import get_instagram_profile_info, download_instagram_video
from .whisper_transcriber import transcrire_video
#from ..celery_config import celery_app

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return jsonify(message="Welcome to the Instagram Scraper API")

@main.route('/get_scripts_by_influencer', methods=['POST'])
def get_scripts_by_influencer():
    data = request.json
    username = data.get('username')
    num_videos = data.get('num_videos')

    if not username or not num_videos:
        return jsonify({'error': 'Missing username or num_videos'}), 400

    num_videos = int(num_videos)
    video_file_paths, status_code = get_instagram_profile_info(username, num_videos)

    if status_code == 200:
        scripts_info = []
        for video_file_path, post in video_file_paths:
            script = transcrire_video(video_file_path)
            video_info = {
                'url': post.url,
                'script': script,
                'likes': post.likes,
                'views': post.video_view_count,
                'comments': post.comments,
                'creator': post.owner_username,
                'date': post.date_utc.isoformat()
            }
            scripts_info.append(video_info)
        return jsonify({'scripts': scripts_info}), 200
    else:
        return jsonify({'error': video_file_paths}), status_code

@main.route('/get_scripts_by_url', methods=['POST'])
def get_scripts_by_url():
    data = request.json
    video_urls = data.get('video_urls')

    if not video_urls:
        return jsonify({'error': 'Missing video URLs'}), 400

    scripts_info = []
    for url in video_urls:
        result, status_code = download_instagram_video(url)
        if status_code == 200:
            video_file_path, post = result
            script = transcrire_video(video_file_path)
            video_info = {
                'url': post.url,
                'script': script,
                'likes': post.likes,
                'views': post.video_view_count,
                'comments': post.comments,
                'creator': post.owner_username,
                'date': post.date_utc.isoformat()
            }
            scripts_info.append(video_info)
        else:
            return jsonify({'error': result}), status_code

    return jsonify({'scripts': scripts_info}), 200
