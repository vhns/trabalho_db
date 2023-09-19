from models import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import INTEGER, VARCHAR, DECIMAL

class Descount(Base):
    __tablename__ = "descount"
    id_descount: Mapped [int] = mapped_column (INTEGER, nullable=False, primary_key=True, autoincrement=True)
    descount_value: Mapped [float] = mapped_column (DECIMAL(6,2), nullable=False)
    descount_description: Mapped [str] = mapped_column (VARCHAR(45), nullable=False)

    payment_descounts: Mapped["Payment_descounts"] = relationship("Payment_descounts", backref="descounts")