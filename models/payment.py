from models import Base, Employee
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import INTEGER, VARCHAR, ForeignKey, DATETIME, DECIMAL
from datetime import date

class Payment(Base):
    __tablename__ = "payment"
    id_payment: Mapped [int] = mapped_column (INTEGER, nullable=False, primary_key=True, autoincrement=True)
    id_employee: Mapped [int] = mapped_column (INTEGER, ForeignKey(Employee.id_employee), nullable=False)
    payment_value: Mapped [float] = mapped_column (DECIMAL(6,2), nullable=False)
    payment_date: Mapped [date] = mapped_column (DATETIME, nullable=False)
    
    payment_descounts: Mapped["Payment_descounts"] = relationship("Payment_descounts", backref="payment")