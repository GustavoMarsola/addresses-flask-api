from flask import Blueprint

from src.services import ServiceAdresses


router1 = Blueprint('address', __name__)
router2 = Blueprint('register-address', __name__)


@router1.get('/addresses')
def route_get_addresses():
    return ServiceAdresses().service_get_address()


@router2.post('/register_address')
def route_get_addresses():
    return ServiceAdresses().service_post_address()
