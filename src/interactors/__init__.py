import abc

from src.entities import UnitOfWork


class Handler(metaclass=abc.ABCMeta):

    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    @abc.abstractmethod
    def handle(self, cmd):
        pass
