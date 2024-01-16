from typing import Union
from pydantic import BaseModel
from time import sleep


class User(BaseModel):
    name: str
    gender: bool
    debit_card_number: float
    email: str


class Database:
    container: dict[int, User]

    def __init__(self) -> None:
        self.container = {}

    async def add_user(self, user: User) -> int:
        if not self.container:
            new_id = 1
        else:
            new_id = max(self.container.keys()) + 1
        sleep(1)
        self.container[new_id] = user
        return new_id

    async def delete_user(self, id: int) -> None:
        sleep(1)
        del self.container[id]

    async def get_user(self, id: int) -> Union[User, None]:
        sleep(1)
        if id not in self.container:
            return None
        return self.container[id]
