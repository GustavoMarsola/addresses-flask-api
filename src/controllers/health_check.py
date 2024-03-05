from flask import Blueprint, jsonify, make_response

router = Blueprint('health_check', __name__)


@router.route("/health_check", methods=['GET'])
def alive():
    return make_response(
        jsonify({
            'message':'hello world!', 
            'status' :'alive'
            }), 200)