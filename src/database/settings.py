import logging

from contextlib             import contextmanager
from sqlalchemy.engine      import create_engine
from sqlalchemy.orm         import sessionmaker, Session

from src.settings import get_settings


_LOGGER = logging.getLogger(__name__)


def create_sync_engine():
    if get_settings().server_settings.environment == 'test':
        return create_engine(
            url = get_settings().database_settings.testing_database_uri
		)
    return create_engine(
        url = get_settings().database_settings.database_uri,
        pool_size     = get_settings().database_settings.database_pool_size,
        max_overflow  = get_settings().database_settings.database_max_overflow,
        pool_pre_ping = True,
        pool_recycle  = get_settings().database_settings.database_pool_recicle_seconds,
        echo          = get_settings().database_settings.database_echo_sql_option,
        )

_engine = create_sync_engine()


_session = sessionmaker(
    bind = _engine,
    class_ = Session,
    autoflush = get_settings().database_settings.database_autoflush,
    autocommit = get_settings().database_settings.database_autocommit,
    expire_on_commit = get_settings().database_settings.database_expire_on_commit,
    future = get_settings().database_settings.database_future
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
