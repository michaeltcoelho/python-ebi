from uuid import UUID
from typing import List

from src.entities.tasks import Task


class Column:

    def __init__(self, column_id: UUID, title: str) -> None:
        self.column_id = column_id
        self.title = title
        self.tasks = List[Task]

    def __str__(self) -> str:
        return f'<Column(id={self.column_id}, title={self.title})>'

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)
