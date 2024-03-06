from sqlalchemy import text
from sqlalchemy.orm import Session

from src.models.address import Address
from src.database.settings import get_connection

#TODO: mudar todos os self.session_db para with get_connection

class RepositoryAddress:
    def __init__(self, session: Session = 1) -> None:
        self.session_db = session
        self.model = Address
        
    
    def execute_statement(self, _sql):
        self.session_db.execute(statement=text(_sql))
        self.session_db.commit()        
    
    
    def get_all_addresses(self) -> list:
        with get_connection() as conn:
            addresses = conn.query(self.model).all()
            return [address.as_dict() for address in addresses]
    
    
    def get_address_by_zipcode(self, zip_code: str) -> dict:
        address = self.session_db.query(self.model).filter_by(zipcode=zip_code).first()
        if address:
            _address = address.as_dict()
            return _address
        else:
            return {}
    
    
    def insert_address(self, insert_model: Address) -> None:
        self.session_db.add(insert_model)
        self.session_db.commit()
    
    
    def update_address(self, zip_code:str, update_model: Address) -> dict:
        address = self.session_db.query(self.model).filter_by(zipcode=zip_code).first() 
        if address:
            for key, value in update_model.__dict__.items():
                if key != '_sa_instance_state' and value is not None:
                    setattr(address, key, value)
            self.session_db.commit()
            return address.as_dict()
        else:
            return {}
    
    
    def delete_address(self, zip_code:str) -> bool:
        address = self.session_db.query(self.model).filter_by(zipcode=zip_code).first() 
        if address:
            self.session_db.delete(address)
            self.session_db.commit()
            return True
        else:
            return False
