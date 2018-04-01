from src.entities.tasks import Task


class Column:

    def __init__(self, column_id, title):
        self.column_id = column_id
        self.title = title
        self.tasks = []

    def __str__(self):
        return f'<Column(id={self.column_id}, title={self.title})>'

    def add_task(self, task):
        self.tasks.append(task)
