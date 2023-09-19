from models import Base, Receiver, Donation_center
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import INTEGER, ForeignKey

class Receiver_center(Base):
    __tablename__ = "receiver_center"
    id_receiver: Mapped [int] = mapped_column(INTEGER, ForeignKey(Receiver.id_receiver), nullable=False, primary_key=True)
    id_center: Mapped [int] = mapped_column(INTEGER, ForeignKey(Donation_center.id_center), nullable=False)