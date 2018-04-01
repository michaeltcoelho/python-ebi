from uuid import uuid4

from src.entities import Repository
from src.entities.boards import Board
from src.interactors.boards import (
    NewBoard, AppendBoardAColumn, create_new_board,
    append_column_to_board,
)


class FakeBoardRepository(Repository):

    def __init__(self):
        self.boards = []

    def add(self, board):
        self.boards.append(board)

    def save(self, board):
        for idx, b in enumerate(self.boards):
            if b.board_id == board.board_id:
                self.boards[idx] = board

    def get(self, board_id):
        for board in self.boards:
            if board.board_id == board_id:
                return board

    def __getitem__(self, index):
        return self.boards[index]


def test_new_board():
    repo = FakeBoardRepository()
    cmd = NewBoard(board_id=uuid4(), title='backlog')
    create_new_board(repo, cmd)
    assert repo[0].board_id == cmd.board_id
    assert repo[0].title == cmd.title


def test_append_column_to_board():
    repo = FakeBoardRepository()
    board = Board(board_id=uuid4(), title='project')
    repo.add(board)
    cmd = AppendBoardAColumn(
        board_id=board.board_id, column_id=uuid4(),
        title='backlog',
    )
    append_column_to_board(repo, cmd)
    assert repo[0].columns[0].column_id == cmd.column_id
    assert repo[0].columns[0].title == cmd.title
