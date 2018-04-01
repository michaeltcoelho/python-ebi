from src.entities.users import User


class Assigment:

    def __init__(self, assign_to, assign_by):
        self.assign_to = assign_to
        self.assign_by = assign_by

    def is_reassignment_from(self, other):
        if other.user_id == self.assign_to.user_id:
            return True
        return False


class Task:

    def __init__(self, task_id, title, description, added_by):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.added_by = added_by
        self.assigments = []

    def __str__(self):
        return f'<Task(id={self.task_id}, title={self.title})>'

    @property
    def assignment(self):
        if len(self.assigments) == 0:
            return None
        return self.assigments[-1]

    def assign(self, assign_to, assign_by):
        previous_assignment = self.assignment
        if previous_assignment is None or\
                not previous_assignment.is_reassignment_from(assign_to):
            self.assigments.append(Assigment(assign_to, assign_by))
