from typing import Union


class ResponseEntity:
    
    RESPONSE_MAP = {
        200: 'OK',
        201: 'Created',
        404: 'Not Found',
        500: 'Internal Server Error'
    }
    
    def __init__(self,
                 status_code: int = 200,
                 status_message: str = '',
                 message: str = '',
                 time_elapsed: float = None,
                 data: Union[dict, list] = {}) -> None:
        self._status_code = status_code
        self._status_message = status_message
        self.message = message
        self.time_elapsed = time_elapsed
        self.data = data
    
    def dict(self) -> dict:
        return {
            'status_code': self._status_code,
            'status_message': self._status_message,
            'message': self.message,
            'time_elapsed': self.time_elapsed,
            'data': self.data
        }

    @property
    def status_code(self):
        return self._status_code

    @status_code.setter
    def status_code(self, new_value):
        # Check if the input is of the correct type
        if new_value not in [200, 201, 404, 500]:
            raise TypeError("Attribute status code must be in the list [200, 201, 404, 500]")

        self._status_code = new_value
    
    def status_message(self):
        return self.RESPONSE_MAP.get(self._status_code, 'Undefined')