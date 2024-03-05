from flask import Blueprint, jsonify, make_response, request
from sqlalchemy import text

from src.models.address import Address
from src.database.settings import get_connection

router = Blueprint('routes', __name__, url_prefix='/api/v1')


@router.route("/addresses", methods=['GET'])
def get_addresses():
    with get_connection() as conn:
        result = conn.execute(text("SELECT id, zipcode, city, state, neighborhood, street  FROM address"))
        addresses = [dict(zip(result.keys(), row)) for row in result]
        print(addresses)
    
    return make_response(jsonify(addresses), 200)


@router.route("/addresses/<zipcode>", methods=['GET'])
def get_address_by_zipcode(zipcode) -> make_response:
    with get_connection() as conn:
        result = conn.query(Address).filter_by(zipcode=zipcode).first()
        if result:
            result = result.__dict__
            result.pop('_sa_instance_state', None)
            result.pop('created_at', None)
            result.pop('updated_at', None)
            return make_response(jsonify(result), 200)
        else:
            return make_response(jsonify({'error': 'Endereço não encontrado'}), 404)


@router.route("/address/register", methods=['POST'])
def register_new_address():
    with get_connection() as conn:
        data = request.json
        
        add_model = Address(
            zipcode = data['zipcode'],
            city = data['city'],
            state = data['state'],
            street = data['street'],
            neighborhood = data['neighborhood']
        )
        
        conn.add(add_model)
        conn.commit()
        
        return make_response(jsonify({'message': 'Success!'}), 201)