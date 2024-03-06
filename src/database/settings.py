import logging
from asyncio import current_task
from contextlib             import contextmanager
from sqlalchemy.engine      import create_engine
from sqlalchemy.orm         import sessionmaker, Session
from sqlalchemy.orm.scoping import scoped_session

from src.settings import get_settings


_LOGGER = logging.getLogger(__name__)


_engine = create_engine(
    url = get_settings().database_settings.database_uri,
)

print(get_settings().database_settings.database_uri)

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
