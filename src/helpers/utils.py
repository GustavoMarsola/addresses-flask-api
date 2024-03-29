from datetime import datetime, timezone, timedelta
from math import isnan
from decimal import Decimal


def set_local_time() -> datetime:
    _offset = timedelta(hours=-3)
    _tz = timezone(offset=_offset)
    return datetime.now(tz=_tz).replace(tzinfo=None)


def read_sql_file(path):             
    fd = open(path, 'r')
    _sql = fd.read()
    fd.close()   
    

    return _sql 


def safeget(dct, *keys):
    for key in keys:
        try:
            dct = dct[key]
        except (KeyError, TypeError):
            return None
    return dct


def serialize(obj: dict) -> dict:
    for key in obj:
        obj[key] = (
            obj[key].isoformat()
            if isinstance(obj[key], datetime)
            else None
            if isinstance(obj[key], float) and isnan(obj[key])
            else float(obj[key])
            if isinstance(obj[key], Decimal)
            else serialize(obj[key]) # serialize recursively 
            if isinstance(obj[key], dict)
            else obj[key]
        ) 
    
    return obj