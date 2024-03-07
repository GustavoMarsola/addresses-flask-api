import logging

from contextlib             import contextmanager
from sqlalchemy.engine      import create_engine
from sqlalchemy.orm         import sessionmaker, Session

from src.settings import get_settings


_LOGGER = logging.getLogger(__name__)


_engine = create_engine(
    url = get_settings().database_settings.database_uri,
    pool_size     = get_settings().database_settings.database_pool_size,
    max_overflow  = get_settings().database_settings.database_max_overflow,
    pool_pre_ping = True,
    pool_recycle  = get_settings().database_settings.database_pool_recicle_seconds,
    echo          = get_settings().database_settings.database_echo_sql_option,
    )

print(get_settings().database_settings.database_uri)
#TODO: PASSAR OS PARAMS DE SESSIONMAKER PARA O SETTINGS INICIAL
_session = sessionmaker(
    bind=_engine,
    class_=Session,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
    future=True
)


@contextmanager
def get_connection():
    try:
        yield _session()
    except Exception as ex:
        _LOGGER.error('roolback session caused by: %s', repr(ex))
        _session().rollback()
        raise
    finally:
        _session().close()
