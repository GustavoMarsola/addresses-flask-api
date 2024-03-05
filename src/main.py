from flask import Flask, jsonify
from flask_restful import Api
# from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException
from werkzeug.exceptions import default_exceptions

from src.controllers.routes.v1 import router as v1_router
from src.controllers.routes.health_check import router as health_check


app = Flask(__name__)

@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    if  isinstance(e, HTTPException):
        code = e.code
    return jsonify(error=str(e)), code

for ex in default_exceptions:
    app.register_error_handler(ex, handle_error)


api = Api(app)
api.prefix = '/api'

app.register_blueprint(v1_router)
app.register_blueprint(health_check)

