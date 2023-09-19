from models import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import INTEGER, VARCHAR, DATE, SMALLINT
from datetime import date

class Person (Base):
    __tablename__ = "person"
    id_person: Mapped [int] = mapped_column (INTEGER, nullable=False, primary_key=True, autoincrement=True)
    person_name: Mapped [str] = mapped_column (VARCHAR(100), nullable=False)
    birth_year: Mapped [date] = mapped_column (DATE, nullable=False)
    street: Mapped [str] = mapped_column (VARCHAR(45), nullable=False)
    house_number: Mapped [int] = mapped_column (SMALLINT, nullable=False)
    neighborhood: Mapped [str] = mapped_column (VARCHAR(45), nullable=False)
    cpf: Mapped[str] = mapped_column (VARCHAR(11), nullable=False)
    name: Mapped[str] = mapped_column (VARCHAR(50), nullable=False)
    sex: Mapped[str] = mapped_column (VARCHAR(1), nullable=False)

    pacient: Mapped["Pacient"] = relationship("Pacient", backref="person")
    receiver: Mapped["Receiver"] = relationship("Receiver", backref="person")
    employee: Mapped["Employee"] = relationship("Employee", backref="person")