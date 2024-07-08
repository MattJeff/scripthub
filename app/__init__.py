import os
from flask import Flask

def install_dependencies():
    import subprocess
    subprocess.call([os.sys.executable, "-m", "pip", "install", "openai-whisper"])

def create_app():
    print("Application is starting...")
    app = Flask(__name__)
    print("Flask app created.")

    # Configuration de l'application
    app.config.from_object('config.Config')

    # Enregistrer les blueprints
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    # Installer openai-whisper dynamiquement au démarrage
    install_dependencies()

    return app
