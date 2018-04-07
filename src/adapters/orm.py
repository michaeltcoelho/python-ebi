from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session, Session, mapper
from sqlalchemy_utils import create_database, drop_database

from src.entities import UnitOfWork, RepositoryContainer
from src.entities.boards import BoardRepository


class SQLAlchemy:

    def __init__(self, uri):
        self.engine = create_engine(uri)
        self._session_maker = scoped_session(sessionmaker(self.engine))

    @property
    def session(self):
        return self._session_maker()

    def drop_schema(self):
        drop_database(self.engine.url)

    def create_schema(self):
        if not hasattr(self, 'metadata'):
            raise ValueError('You must call `configure`'
                             'before creating schema.')
        else:
            create_database(self.engine.url)
            self.metadata.create_all()

    def configure(self):
        self.configure_mappings()

    def configure_mappings(self):
        self.metadata = MetaData(self.engine)


class SQLAlchemyUnitOfWork(UnitOfWork):

    def __init__(self, session):
        self.session = session

    def commit(self):
        self.session.flush()
        self.session.commit()

    def rollback(self):
        self.session.rollback()

    @property
    def repositories(self):
        return RepositoryContainer(self.session)
