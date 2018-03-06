from uuid import UUID


class User:

    def __init__(self, user_id: UUID, name: str, email: str) -> None:
        self.user_id = user_id
        self.name = name
        self.email = email
    
    def __str__(self):
        return f'<User(id={self.user_id}, email={self.email})>'
