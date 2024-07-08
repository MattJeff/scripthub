from install_dependencies import install_openai_whisper

# Installer openai-whisper si ce n'est pas déjà fait
install_openai_whisper()

# Maintenant, vous pouvez importer whisper
import whisper

def transcrire_video(video_file_path):
    model = whisper.load_model("base")
    result = model.transcribe(video_file_path)
    return result["text"]
