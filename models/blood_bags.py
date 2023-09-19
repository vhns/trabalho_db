from models import Base, pacient, employee
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import INTEGER, VARCHAR, DATETIME, ForeignKey
from datetime import datetime

class Blood_bags (Base):
    __tablename__ = "blood_bags"
    id_bags: Mapped [int] = mapped_column(INTEGER, nullable=False, primary_key=True, autoincrement=True)
    id_employee: Mapped [int] = mapped_column(INTEGER, ForeignKey(employee.Employee.id_employee), nullable=False)
    id_pacient: Mapped [int] = mapped_column(INTEGER, ForeignKey(pacient.Pacient.id_pacient), nullable=False)
    blood_type: Mapped [str] = mapped_column(VARCHAR(3), nullable=False)
    entry_date: Mapped [datetime] = mapped_column(DATETIME, nullable=False)
    departura_time:  Mapped [datetime] = mapped_column(DATETIME, nullable=False)

    blood_storage: Mapped ["Blood_storage"] = relationship("Blood_storage", backref="blood_bags", uselist=False)
    receiver: Mapped ["Receiver"] = relationship("Receiver", backref="blood_bags", uselist=False)