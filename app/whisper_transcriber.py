import whisper

def transcrire_video(video_file_path):
    model = whisper.load_model("large")
    result = model.transcribe(video_file_path)
    script = result['text']
    return script
