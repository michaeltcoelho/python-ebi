

class TaskReporter:

    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email

    def __str__(self):
        return f'<TaskReporter(name={self.name}, email={self.email})>'


class Task:

    def __init__(self, name: str, reporter: TaskReporter,
                 ordering: int=0) -> None:
        self.name = name
        self.ordering = ordering
        self.assigments = []

    def __str__(self):
        return f'<Task(name={self.name}, ordering={self.ordering})>'
