from models import Base, person
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import INTEGER, VARCHAR, ForeignKey

class Pacient(Base):
    __tablename__ = "pacient"
    id_pacient: Mapped [int] = mapped_column (INTEGER, ForeignKey(person.Person.id_person), nullable=False, primary_key=True)
    blood_type: Mapped [str] = mapped_column (VARCHAR(3), nullable=False)

    pacient_center: Mapped ["Pacient_center"] = relationship("Pacient_center", backref="pacient")
    blood_bags: Mapped ["Blood_bags"] = relationship("Blood_bags", backref="pacient")