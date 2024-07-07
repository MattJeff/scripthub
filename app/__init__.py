from flask import Flask

def create_app():
    app = Flask(__name__)

    # Configuration de l'application
    app.config.from_object('config.Config')

    # Enregistrer les blueprints
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

app = create_app()

