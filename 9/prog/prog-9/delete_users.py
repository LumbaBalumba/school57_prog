from sqlalchemy.orm import Session
from sqlalchemy import select
from db_init import Address, engine, User

session = Session(engine)

user = session.get(User, 3)
addresses = select(Address).where(Address.user_id == 3)
for address in session.scalars(addresses):
    print(address)

session.query(User).filter_by(id=3).delete()

session.commit()
