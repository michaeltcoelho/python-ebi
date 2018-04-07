import abc

from src.entities import UnitOfWork


class Handler(abc.ABC):

    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    @abc.abstractmethod
    def handle(self, cmd):
        pass
