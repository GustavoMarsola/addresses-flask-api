from flask import Blueprint, jsonify, make_response

router = Blueprint('health_check', __name__, url_prefix='/api')

@router.get("/health_check")
def alive() -> make_response:
    return make_response(
        jsonify({
            'message':'hello world!', 
            'status' :'alive'
            }), 200)