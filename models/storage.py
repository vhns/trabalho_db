from models import Base, donation_center
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import INTEGER, VARCHAR, SMALLINT, ForeignKey

class Storage(Base):
    __tablename__ = "storage"
    id_storage: Mapped [int] = mapped_column(INTEGER, nullable=False,primary_key=True, autoincrement=True)
    id_center: Mapped [int] = mapped_column(INTEGER, ForeignKey(donation_center.Donation_center.id_center), nullable=False)
    street: Mapped [str] = mapped_column(VARCHAR(100), nullable=False)
    s_number: Mapped [int] = mapped_column(SMALLINT, nullable=False)
    neighborhood: Mapped [str] = mapped_column(VARCHAR(45), nullable=False)

    blood_storage: Mapped ["Blood_storage"] = relationship("Blood_storage", backref="storage")