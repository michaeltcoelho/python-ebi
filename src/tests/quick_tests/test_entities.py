from uuid import uuid4

from src.entities.boards import Board
from src.entities.columns import Column
from src.entities.tasks import Task
from src.entities.users import User


def test_add_columns_to_a_board():
    board = Board(uuid4(), 'Project X')
    board.add_column(Column(uuid4(), 'TODO'))
    board.add_column(Column(uuid4(), 'WIP'))
    board.add_column(Column(uuid4(), 'DONE'))
    assert len(board.columns) == 3


def test_add_tasks_to_a_column():
    column = Column(uuid4(), 'TODO')
    added_by = User(uuid4(), 'moo', 'moo@gmail.com')
    column.add_task(Task(uuid4(), 'Title', 'Description...', added_by))
    column.add_task(Task(uuid4(), 'Title', 'Description...', added_by))
    assert len(column.tasks) == 2


def test_assign_task_to_user():
    user = User(uuid4(), 'User', 'user@gmail.com')
    task = Task(uuid4(), 'Title', 'Desc', user)
    task.assign(user, user)
    assert task.assignment.assign_to == user
    assert task.assignment.assign_by == user


def test_do_not_assign_to_the_same_user_twice():
    user = User(uuid4(), 'User', 'user@gmail.com')
    task = Task(uuid4(), 'Title', 'Desc', user)
    task.assign(user, user)
    assert len(task.assigments) == 1
    task.assign(user, user)
    assert len(task.assigments) == 1
