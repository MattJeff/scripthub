import os
import subprocess

def install_openai_whisper():
    try:
        import whisper
    except ImportError:
        try:
            subprocess.check_call([os.sys.executable, "-m", "pip", "install", "openai-whisper"])
        except subprocess.CalledProcessError as e:
            print(f"Failed to install openai-whisper: {e}")

if __name__ == '__main__':
    install_openai_whisper()
