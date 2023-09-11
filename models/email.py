from models import Base, Person
from sqlalchemy import VARCHAR, INTEGER, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

class Email(Base):
    __tablename__ = "email"
    id: Mapped[int] = mapped_column(INTEGER,nullable=False,primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(VARCHAR(100), nullable=False, unique=True)
    person_id: Mapped[int] = mapped_column(INTEGER, ForeignKey(Person.id), nullable=False)