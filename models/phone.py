from models import Base, Person
from sqlalchemy import SMALLINT, BIGINT, INTEGER, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


class Phone(Base):
    __tablename__ = "phone"
    id: Mapped[int] = mapped_column(INTEGER,nullable=False,primary_key=True, autoincrement=True)
    country_code: Mapped[int] = mapped_column(SMALLINT, nullable=False)
    ddd: Mapped[int] = mapped_column(SMALLINT, nullable=False)
    phone_number: Mapped[int] = mapped_column(BIGINT, nullable=False)
    person_id: Mapped[int] = mapped_column(INTEGER, ForeignKey(Person.id), nullable=False)