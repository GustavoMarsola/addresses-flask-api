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
    connect_args = _CONNECT_ARGS_SQLITE,
    
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
def get_session():
    """
    Get repositories session from factory and factory will do rollback if an exception are raised and always will
    remove session from registry.
    """
    _sync_scoped_session: scoped_session = scoped_session(session_factory=_session)
    try:
        yield _sync_scoped_session()
        _sync_scoped_session.commit()
    except Exception as ex:
        _sync_scoped_session.rollback()
        raise
    finally:
        _sync_scoped_session.remove()


@contextmanager
def get_connection():
    """
    Get connection from engine and engine will do rollback if an exception are raised.
    """
    with _engine.connect() as connection:
        with connection.begin():
            yield connection


