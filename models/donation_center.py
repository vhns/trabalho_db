from models import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import INTEGER, VARCHAR, SMALLINT, TIME
from datetime import time

class Donation_center(Base):
    __tablename__ = "donation_center"
    id_center: Mapped [int] = mapped_column(INTEGER, nullable=False, primary_key=True, autoincrement=True)
    center_name: Mapped [str] = mapped_column(VARCHAR(45), nullable=False)
    street: Mapped [str] = mapped_column(VARCHAR(100), nullable=False)
    center_number: Mapped [int] = mapped_column(SMALLINT, nullable=False)
    neighborhood: Mapped [str] = mapped_column(VARCHAR(45), nullable=False)
    working_period_s: Mapped [time] = mapped_column(TIME, nullable=False)
    working_period_e: Mapped [time] = mapped_column(TIME, nullable=False)

    employee: Mapped ["Employee"] = relationship("Emplyee", backref="donation_center")
    storage: Mapped ["Storage"] = relationship("Storage", backref="donation_center")
    pacient_center: Mapped ["Pacient_center"] = relationship("Pacient_center", backref="donation_center")
    receiver_center: Mapped ["Receiver_center"] = relationship("Receiver_center", backref="donation_center")
