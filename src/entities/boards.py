from uuid import UUID
from typing import List

from src.entities.columns import Column


class Board:

    def __init__(self, board_id: UUID, title: str) -> None:
        self.board_id = board_id
        self.title = title
        self.columns = List[Column]

    def __str__(self) -> str:
        return f'<Board(title={self.title})>'

    def add_column(self, column: Column) -> None:
        self.columns.append(column)
