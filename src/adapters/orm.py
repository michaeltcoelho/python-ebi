import typing

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session, Session, mapper
from sqlalchemy_utils import create_database, drop_database


SessionFactory = typing.Callable[[], Session]


class SQLAlchemy:

    def __init__(self, uri: str) -> None:
        self.engine = create_engine(uri)
        self.metadata = MetaData(self.engine)
        self._session_maker = scoped_session(sessionmaker(self.engine), )

    @property
    def session(self) -> SessionFactory:
        return self._session_maker()

    def drop_schema(self) -> None:
        drop_database(self.engine.url)
    
    def create_schema(self) -> None:
        create_database(self.engine.url)
        self.metadata.create_all()

    def configure(self) -> None:
        self.configure_mappings()

    def configure_mappings(self) -> None:
        pass
