from models import Base, Blood_bags, storage
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import INTEGER, ForeignKey

class Blood_storage(Base):
    __tablename__ = "blood_storage"
    id_bags: Mapped [int] = mapped_column(INTEGER, ForeignKey(Blood_bags.id_bags), nullable=False, primary_key=True)
    id_storage : Mapped [int] = mapped_column(INTEGER, ForeignKey(storage.Storage.id_storage), nullable=False)

