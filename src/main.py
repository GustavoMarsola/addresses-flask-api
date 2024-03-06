from flask import Flask, jsonify
# from flask_restful import Api
# from werkzeug.exceptions import HTTPException
# from werkzeug.exceptions import default_exceptions

from src.controllers.routes.v1 import v1
from src.controllers.routes.health_check import router as health_check



def create_app():
    app = Flask(__name__)
    app.register_blueprint(health_check)
    app.register_blueprint(v1)
    
    return app

_app = create_app()
# @app.errorhandler(Exception)
# def handle_error(e):
#     code = 500
#     if  isinstance(e, HTTPException):
#         code = e.code
#     return jsonify(error=str(e)), code

# for ex in default_exceptions:
#     app.register_error_handler(ex, handle_error)

# app.register_blueprint(v1_router)
# app.register_blueprint(health_check)


