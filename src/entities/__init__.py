import abc


class UnitOfWork(abc.ABC):

    @abc.abstractmethod
    def commit(self):
        pass

    @abc.abstractmethod
    def rollback(self):
        pass

    @property
    @abc.abstractmethod
    def repositories(self):
        pass


class Repository(abc.ABC):

    def __init__(self, session):
        self.session = session


class RepositoryContainer:

    def __init__(self, session):
        self.session = session

    @property
    def boards(self):
        from src.entities.boards import BoardRepository
        return BoardRepository(self.session)
