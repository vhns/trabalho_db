from models import Base, Pacient, Donation_center
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import INTEGER, ForeignKey

class Pacient_center(Base):
    __tablename__ = "pacient_center"
    id_pacient: Mapped [int] = mapped_column(INTEGER, ForeignKey(Pacient.id_pacient), nullable=False, primary_key=True)
    id_center: Mapped [int] = mapped_column(INTEGER, ForeignKey(Donation_center.id_center), nullable=False)