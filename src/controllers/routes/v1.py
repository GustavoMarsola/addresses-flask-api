from flask import Blueprint, Request

from src.repositories.api_repository import RepositoryAPI
from src.repositories.address_repository import RepositoryAddress

from src.services import ServiceAdresses


router = Blueprint('routes', __name__, url_prefix='/api/v1')


@router.get('/addresses')
def route_get_addresses():
    return ServiceAdresses(request=Request).service_get_address()
