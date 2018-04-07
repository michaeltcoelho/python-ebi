from src.entities import UnitOfWork, Repository


class FakeUnitOfWork(UnitOfWork):

    def __init__(self):
        self.was_commited = False
        self.was_rolled_back = False

    def commit(self):
        self.was_commited = True

    def rollback(self):
        self.was_rolled_back = True

    @property
    def repositories(self):
        return FakeRepositoryContainer()


class FakeRepositoryContainer:

    @property
    def boards(self):
        return FakeBoardRepository()


class FakeBoardRepository(Repository):

    BOARDS = []

    def __init__(self):
        super().__init__(None)

    def add(self, board):
        self.BOARDS.append(board)

    def save(self, board):
        for idx, b in enumerate(self.BOARDS):
            if b.board_id == board.board_id:
                self.BOARDS[idx] = board

    def get(self, board_id):
        for board in self.BOARDS:
            if board.board_id == board_id:
                return board

    def __getitem__(self, index):
        return self.BOARDS[index]

    def __len__(self):
        return len(self.BOARDS)
