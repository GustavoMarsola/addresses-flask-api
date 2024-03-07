from sqlalchemy import text

from src.models.address import Address
from src.database.settings import get_connection


class RepositoryAddress:
    def __init__(self) -> None:
        self.model = Address
        
    
    def execute_statement(self, _sql):
        with get_connection() as conn:
            conn.execute(statement=text(_sql))
            conn.commit()        
    
    
    def get_all_addresses(self) -> list:
        with get_connection() as conn:
            addresses = conn.query(self.model).all()
            return [address.as_dict() for address in addresses]
    
    
    def get_address_by_zipcode(self, zip_code: str) -> dict:
        with get_connection() as conn:
        
            address = conn.query(self.model).filter_by(zipcode=zip_code).first()
            if address:
                _address = address.as_dict()
                return _address
            else:
                return {}
    
    
    def insert_address(self, insert_model: Address) -> None:
        with get_connection() as conn:
        
            conn.add(insert_model)
            conn.commit()
    
    
    def update_address(self, zip_code:str, update_model: Address) -> dict:
        with get_connection() as conn:
            address = conn.query(self.model).filter_by(zipcode=zip_code).first() 
            if address:
                for key, value in update_model.__dict__.items():
                    if key != '_sa_instance_state' and value is not None:
                        setattr(address, key, value)
                conn.commit()
                return address.as_dict()
            else:
                return {}
    
    
    def delete_address(self, zip_code:str) -> bool:
        with get_connection() as conn:
        
            address = conn.query(self.model).filter_by(zipcode=zip_code).first() 
            if address:
                conn.delete(address)
                conn.commit()
                return True
            else:
                return False
