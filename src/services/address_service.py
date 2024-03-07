from dataclasses import dataclass
from flask import Request, make_response, jsonify

from src.repositories.api_repository import RepositoryAPI
from src.services.service_base import error_handler
from src.helpers.utils import set_local_time


@dataclass
class ServiceAdresses:
    request: Request
    
    @error_handler
    def service_get_address(self):
        self.repository = RepositoryAPI()
        t0  = set_local_time()
        msg = ''
        all_addresses = self.repository.tbl_address.get_all_addresses()
        
        if len(all_addresses) == 0:
            msg += 'no zipcode registered yet'
            return make_response(jsonify({'message': msg}), 200)
        
        t1  = set_local_time()
        
        print(f'Executed in {(t1-t0).total_seconds()} seconds')
        return make_response(jsonify({'message': 'Data collected successfully','amount_addresses': len(all_addresses),'data': all_addresses}), 200)
