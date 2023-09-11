from models import Base, Person
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import INTEGER, CHAR, ForeignKey

class Client(Base):
    __tablename__ = "client"
    id: Mapped[int] = mapped_column(INTEGER, ForeignKey(Person.id), 
                                    primary_key=True, nullable=False, autoincrement=True)
    cnh: Mapped[str] = mapped_column(CHAR(12), nullable=False, unique=True)
    