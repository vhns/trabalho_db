from models import Base, Person, blood_bags
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import INTEGER, VARCHAR, ForeignKey, DATETIME
from datetime import date


class Receiver(Base):
    __tablename__ = "receiver"
    id_receiver: Mapped [int] = mapped_column (INTEGER, ForeignKey(Person.id_person), nullable=False, primary_key=True)
    id_bags: Mapped [int] = mapped_column (INTEGER, ForeignKey(blood_bags.Blood_bags.id_bags), nullable=False)
    date_recieve: Mapped [date] = mapped_column (DATETIME, nullable=False)
    blood_type: Mapped [str] = mapped_column (VARCHAR(3), nullable=False)

    receiver_center: Mapped ["Receiver_center"] = relationship("Receiver_center", backref="receiver")