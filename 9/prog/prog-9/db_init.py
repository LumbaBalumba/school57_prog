from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from typing import List, Optional

from sqlalchemy import create_engine


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20))
    surname: Mapped[Optional[str]]

    addresses: Mapped[List["Address"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.surname}"

    def __repr__(self) -> str:
        return f"{self.id} {self.name} {self.surname}"


class Address(Base):
    __tablename__ = "address_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str]

    user: Mapped["User"] = relationship(back_populates="addresses")

    user_id: Mapped[int] = mapped_column(ForeignKey("user_table.id"))

    def __str__(self) -> str:
        return f"{self.id} {self.email}"

    def __repr__(self) -> str:
        return f"{self.id} {self.email}"


engine = create_engine("sqlite:///test.db")

if __name__ == "__main__":
    Base.metadata.create_all(engine)
