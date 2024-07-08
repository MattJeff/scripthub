import instaloader
import os

def get_instagram_profile_info(username, num_videos):
    L = instaloader.Instaloader()

    try:
        profile = instaloader.Profile.from_username(L.context, username)
        if profile.is_private:
            return "Erreur : Le profil est privé et ne peut pas être consulté.", 403

        videos = []
        for post in profile.get_posts():
            if post.is_video:
                videos.append(post)
                if len(videos) >= num_videos:
                    break

        if not videos:
            return "Erreur : Aucune vidéo trouvée sur ce profil.", 404

        video_paths = []
        for i, video in enumerate(videos, 1):
            video_path = f"{username}_video_{i}"
            L.download_post(video, target=video_path)
            video_file = [f for f in os.listdir(video_path) if f.endswith('.mp4')][0]
            video_file_path = os.path.join(video_path, video_file)
            video_paths.append((video_file_path, video))

        return video_paths, 200

    except instaloader.exceptions.ProfileNotExistsException:
        return "Erreur : Le profil n'existe pas. Veuillez vérifier le nom d'utilisateur et réessayer.", 404
    except Exception as e:
        return f"Une erreur est survenue : {e}", 500

def download_instagram_video(url):
    L = instaloader.Instaloader()

    try:
        post = instaloader.Post.from_shortcode(L.context, url.split('/')[-2])
        if not post.is_video:
            return "Erreur : L'URL fournie ne correspond pas à une vidéo.", 400

        video_path = f"{post.owner_username}_video_{post.shortcode}"
        L.download_post(post, target=video_path)
        video_file = [f for f in os.listdir(video_path) if f.endswith('.mp4')][0]
        video_file_path = os.path.join(video_path, video_file)

        return (video_file_path, post), 200

    except instaloader.exceptions.PostNotExistsException:
        return "Erreur : La vidéo n'existe pas. Veuillez vérifier le lien et réessayer.", 404
    except Exception as e:
        return f"Une erreur est survenue : {e}", 500
