from flask import Blueprint, jsonify, request

from src.models.address import Address
from src.database.settings import get_connection

routes = Blueprint('routes', __name__)


@routes.route("/addresses", methods=['GET'])
def get_addresses():
    return


@routes.route("/addresses/<str:zipcode>", methods=['GET'])
def get_address_by_zipcode(_zipcode):
    with get_connection() as conn:
        query = conn.query(Address).filter_by(zipcode=_zipcode)
    return