

class Column:

    def __init__(self, name: str, ordering: int=0) -> None:
        self.name = name
        self.ordering = ordering
        self.tasks = []

    def __str__(self) -> str:
        return f'<Column(name={self.name}, ordering={self.ordering})>'
