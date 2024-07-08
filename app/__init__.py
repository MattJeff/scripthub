import os
import subprocess
from flask import Flask
#from ..celery_config import celery_app

def install_openai_whisper():
    try:
        subprocess.check_call([os.sys.executable, "-m", "pip", "install", "openai-whisper"])
    except subprocess.CalledProcessError as e:
        print(f"Failed to install openai-whisper: {e}")

def create_app():
    print("Application is starting...")
    app = Flask(__name__)
    print("Flask app created.")


    # Configuration de l'application
    app.config.from_object('config.Config')

    # Enregistrer les blueprints
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

# Installer openai-whisper dynamiquement au démarrage
install_openai_whisper()

app = create_app()

# Initialiser Celery avec l'application Flask
#celery_app.conf.update(app.config)

