from models import Base, Payment, descounts
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import INTEGER, ForeignKey

class Payment_descounts(Base):
    __tablename__ = "payment_descounts"
    id_payment: Mapped [int] = mapped_column (INTEGER, ForeignKey(Payment.id_payment) ,nullable=False, primary_key=True)
    id_descount: Mapped [int] = mapped_column (INTEGER, ForeignKey(descounts.Descount.id_descount), nullable=False)