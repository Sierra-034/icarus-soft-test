import os
from flask import Flask
# from config import set_configuration
from src.routes import api_blueprint
from src.models import db, person_model, bitacora_model


def create_app():
    app = Flask(__name__)
    app.register_blueprint(api_blueprint)
    env_config = os.getenv('APP_SETTINGS', 'src.config.DevelopmentConfig')
    app.config.from_object(env_config)

    with app.app_context():
        db.init_app(app)
        db.create_all()
        db.session.commit()
    
    return app