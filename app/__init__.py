import os
import subprocess
from flask import Flask

def install_openai_whisper():
    try:
        subprocess.check_call([os.sys.executable, "-m", "pip3", "install", "openai-whisper"])
    except subprocess.CalledProcessError as e:
        print(f"Failed to install openai-whisper: {e}")

def create_app():
    app = Flask(__name__)

    # Configuration de l'application
    app.config.from_object('config.Config')

    # Enregistrer les blueprints
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

# Installer openai-whisper dynamiquement au démarrage
install_openai_whisper()

app = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
