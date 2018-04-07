from uuid import uuid4

from src.entities.boards import Board
from src.interactors.boards import (
    NewBoard, AppendColumnToBoard, NewBoardHandler,
    AppendColumnToBoardHandler,
)

from .adapters import FakeUnitOfWork


def test_new_board():
    uow = FakeUnitOfWork()
    new_board_handler = NewBoardHandler(uow)
    cmd = NewBoard(board_id=uuid4(), title='backlog')
    new_board_handler.handle(cmd)
    board = uow.repositories.boards.get(cmd.board_id)
    assert board.title == cmd.title


def test_append_column_to_board():
    uow = FakeUnitOfWork()

    board = Board(board_id=uuid4(), title='project')
    uow.repositories.boards.add(board)

    append_new_column_handler = AppendColumnToBoardHandler(uow)
    cmd = AppendColumnToBoard(
        board_id=board.board_id,
        column_id=uuid4(),
        title='backlog',
    )

    append_new_column_handler.handle(cmd)

    updated_board = uow.repositories.boards.get(board.board_id)
    assert len(updated_board.columns) == 1
