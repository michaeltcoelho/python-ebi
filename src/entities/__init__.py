import abc


class UnitOfWork(abc.ABC):

    @abc.abstractmethod
    def commit(self):
        pass

    @abc.abstractmethod
    def rollback(self):
        pass


class Repository(abc.ABC):

    def __init__(self, session):
        self.session = session
