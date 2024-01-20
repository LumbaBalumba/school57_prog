from sqlalchemy import select
from sqlalchemy.orm import Session
from db_init import Address, engine, User

session = Session(engine)

users = session.query(User, Address).filter(
    User.name.in_(["user", "user1", "user2"])
    & (User.id % 2 == 1)
    & (User.surname == "surname")
    | (Address.id <= 10)
)

for user in users:
    print(user)

users = select(User).where(User.name != "i3alumba")

for user in session.scalars(users):
    print(user)

users = session.query(User, Address).filter(
    User.name.in_(["user", "user1"]) & User.id == Address.user_id
)
print("_________")
for user in users:
    print(user)

users = select(Address).join(Address.user).where(User.name.in_(["user", "user1"]))

print("_________")
for user in session.scalars(users):
    print(user)
