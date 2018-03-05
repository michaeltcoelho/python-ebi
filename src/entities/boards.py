

class Board:

    def __init__(self, name: str) -> None:
        self.name = name
        self.columns = []

    def __str__(self) -> str:
        return f'<Board(name={self.name})>'
