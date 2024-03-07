from flask import Blueprint
from src.controllers.routes.v1.address import router1 as get_addresses_router, router2 as post_address_router

v1 = Blueprint('v1', __name__, url_prefix='/api/v1')
v1.register_blueprint(get_addresses_router)
v1.register_blueprint(post_address_router)