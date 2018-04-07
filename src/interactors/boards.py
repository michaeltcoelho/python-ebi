from uuid import UUID
from typing import NamedTuple

from src.entities.boards import Board
from src.entities.columns import Column

from src.interactors import Handler


class NewBoard(NamedTuple):
    board_id: UUID
    title: str


class AppendColumnToBoard(NamedTuple):
    board_id: UUID
    column_id: UUID
    title: str


class NewBoardHandler(Handler):

    def handle(self, cmd: NewBoard):
        board = Board(board_id=cmd.board_id, title=cmd.title)
        self.uow.boards.add(board)
        self.uow.commit()


class AppendColumnToBoardHandler(Handler):

    def handle(self, cmd: AppendColumnToBoard):
        board = self.uow.boards.get(cmd.board_id)
        board.add_column(Column(cmd.column_id, cmd.title))
        self.uow.boards.add(board)
        self.uow.commit()
