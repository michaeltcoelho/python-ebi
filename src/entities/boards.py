from src.entities import Repository


class Board:

    def __init__(self, board_id, title):
        self.board_id = board_id
        self.title = title
        self.columns = []

    def __str__(self):
        return f'<Board(title={self.title})>'

    def add_column(self, column):
        self.columns.append(column)


class BoardRepository(Repository):

    def add(self, board):
        pass

    def get(self, board_id):
        pass
