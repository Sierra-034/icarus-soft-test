from flask import Blueprint
from src.routes.person_routes import persons

api_blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api_blueprint.register_blueprint(persons)
