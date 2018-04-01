from uuid import UUID
from typing import NamedTuple

from src.entities import Repository
from src.entities.boards import Board
from src.entities.columns import Column


class NewBoard(NamedTuple):
    board_id: UUID
    title: str


class AppendBoardAColumn(NamedTuple):
    board_id: UUID
    column_id: UUID
    title: str


def create_new_board(repo: Repository, cmd: NewBoard):
    board = Board(board_id=cmd.board_id, title=cmd.title)
    repo.add(board)


def append_column_to_board(repo: Repository, cmd: AppendBoardAColumn):
    board = repo.get(board_id=cmd.board_id)
    board.add_column(Column(column_id=cmd.column_id, title=cmd.title))
    repo.save(board)
