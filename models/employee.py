from models import Base, Person
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import INTEGER, DECIMAL, ForeignKey

class Employee(Base):
    __tablename__ = "employee"
    id: Mapped[int] = mapped_column(INTEGER, ForeignKey(Person.id), 
                                    primary_key=True, nullable=False, autoincrement=True)
    salary: Mapped[float] = mapped_column(DECIMAL(8,2), nullable=False)
    comission: Mapped[float] = mapped_column(DECIMAL(3,2))
    