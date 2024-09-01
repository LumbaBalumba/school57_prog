from sqlalchemy.orm import Session
from db_init import engine, User, Address

session = Session(engine)

user1 = User(
    name="user",
    surname="smaple_surname",
    addresses=[Address(email="sample_email@i3alumba.org")],
)

user2 = User(
    name="Lumba",
    addresses=[
        Address(email="i3alumba@gmail.com"),
        Address(email="i3alumba@yandex.com"),
    ],
)

user3 = User(name="user", surname="surname", addresses=[Address(email="ttt")])

user4 = User(name="user1", surname="surname", addresses=[Address(email="ttttt")])

session.add_all([user1, user2, user3, user4])
session.commit()

session.close()
