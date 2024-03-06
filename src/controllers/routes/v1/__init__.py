from flask import Blueprint
from src.controllers.routes.v1.address import router as add_router

v1 = Blueprint('v1', __name__, url_prefix='/api/v1')
v1.register_blueprint(add_router)