from flask import Flask
from config import config_dict
from routes import api_blueprint
from models import db, person_model, bitacora_model


def create_app(environment=None):
    app = Flask(__name__)
    app.config.from_object(environment)
    app.register_blueprint(api_blueprint)

    with app.app_context():
        db.init_app(app)
        db.create_all()
        db.session.commit()
    
    return app

if __name__ == '__main__':
    environment = config_dict['development']
    app = create_app(environment)
    app.run()
