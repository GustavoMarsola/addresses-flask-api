from dataclasses import dataclass
from flask import make_response, jsonify, request

from src.repositories.api_repository import RepositoryAPI
from src.models.address import Address
from src.services.service_base import error_handler
from src.helpers.utils import set_local_time


@dataclass
class ServiceAdresses:
    repository = RepositoryAPI()
    msg = ''
    
    @error_handler
    def service_get_address(self):
        all_addresses = self.repository.tbl_address.get_all_addresses()
        
        if len(all_addresses) == 0:
            self.msg += 'No zipcode registered yet'
            return make_response(jsonify({'message': self.msg}), 200)

        return make_response(jsonify({'message': 'Data collected successfully','amount_addresses': len(all_addresses),'data': all_addresses}), 200)
    
    
    @error_handler
    def service_post_address(self):
        # Receiving data
        data = request.get_json(force=True)
        # Must have
        _zipcode = data.get('zipcode')
        _city = data.get('city')
        _state = data.get('state')
        if None in [_zipcode, _city, _state]:
            return make_response(jsonify({'message': 'Address must contain zipcode, city and state'}), 500)
        # Nullable is possible
        _street = data.get('street')
        _neighborhood = data.get('neighborhood')
        
        post_model = Address(
            zipcode = _zipcode,
            city = _city,
            state = _state,
            street = _street,
            neighborhood = _neighborhood
        )
        
        posting = self.repository.tbl_address.insert_address(insert_model=post_model)
        
        if posting is False:
            return make_response(jsonify({'message': 'Fail to insert data'}), 500)
            
        return make_response(jsonify({'message': 'Data registered successfully','amount_registries': 1, 'data': post_model.as_dict()}), 200)
