from app import create_app
from app.models import db, Creator, Video, UserCreator
from app.scraper import get_instagram_profile_info
from app.whisper_transcriber import transcrire_video
import os

app = create_app()

def check_new_videos():
    with app.app_context():
        user_creators = UserCreator.query.filter_by(auto_track=True).all()
        for user_creator in user_creators:
            creator = Creator.query.get(user_creator.creator_id)
            video_file_paths, status_code = get_instagram_profile_info(creator.username, 1)
            if status_code == 200:
                for video_file_path, post in video_file_paths:
                    if not Video.query.filter_by(url=post.url).first():
                        script = transcrire_video(video_file_path)
                        video_info = get_video_info(post)
                        new_video = Video(
                            url=post.url,
                            text=script,
                            creator_id=creator.id,
                            likes=post.likes,
                            views=post.video_view_count,
                            comments=post.comments
                        )
                        db.session.add(new_video)
        db.session.commit()

if __name__ == '__main__':
    check_new_videos()
