import traceback
from flask import make_response, jsonify
from functools import wraps
from typing import Callable


def error_handler(func: Callable):
    """Decorator to handle an exception"""

    @wraps(func)
    def wrapped_func(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            error = {"error_type":   str(type(e).__name__), 
                        "error":        str(e),  
                        "error_detail": str(traceback.format_exc())
                    }
            
            return make_response(jsonify(error), 500)

    return wrapped_func