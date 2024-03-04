import logging
from contextlib             import contextmanager
from sqlalchemy.engine      import create_engine
from sqlalchemy.orm         import sessionmaker, Session
from sqlalchemy.orm.scoping import scoped_session

from src.settings import get_settings


_CONNECT_ARGS_SQLITE = {'check_same_thread': False}

_LOGGER = logging.getLogger(__name__)


_engine = create_engine(
    url = get_settings().database_settings.database_uri,
    connect_args = _CONNECT_ARGS_SQLITE
)


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
        _session().rollback()
    finally:
        _session().close()


