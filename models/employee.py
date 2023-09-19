from models import Base, person, donation_center
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import INTEGER, VARCHAR, ForeignKey, TIME
from datetime import time

class Employee(Base):
    __tablename__ = "employee"
    id_employee: Mapped [int] = mapped_column (INTEGER, ForeignKey(person.Person.id_person), primary_key=True)
    id_donation_center: Mapped [int] = mapped_column (INTEGER, ForeignKey(donation_center.Donation_center.id_center), nullable=False)
    e_function: Mapped [str] = mapped_column (VARCHAR(45), nullable=False)
    work_time_s: Mapped [time] = mapped_column (TIME, nullable=False)
    work_time_e: Mapped [time] = mapped_column (TIME, nullable=False)

    payment: Mapped ["Payment"] = relationship("Payment", backref="employee")
    blood_bags: Mapped ["Blood_bags"] = relationship("Blood_bags", backref="employee")