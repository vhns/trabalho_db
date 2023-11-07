from datetime import date
from models import Base, person, blood_bags
from sqlalchemy.orm import Mapped, mapped_column, relationship, aliased
from sqlalchemy import INTEGER, VARCHAR, ForeignKey, Date, insert, select, func

class Pacient(Base):
    __tablename__ = "pacient"
    id_pacient: Mapped [int] = mapped_column (INTEGER, ForeignKey(person.Person.id_person), nullable=False, primary_key=True)
    blood_type: Mapped [str] = mapped_column (VARCHAR(3), nullable=False)

    pacient_center: Mapped ["Pacient_center"] = relationship("Pacient_center", backref="pacient")
    blood_bags: Mapped ["Blood_bags"] = relationship("Blood_bags", backref="pacient")
    
    def insert_pacient(self, engine):
        conn = engine.connect()
        conn.execute(insert(Pacient).values(id_pacient=7, blood_type='B-'))
        conn.execute(insert(Pacient).values(id_pacient=8, blood_type='B-'))
        conn.execute(insert(Pacient).values(id_pacient=9, blood_type='B-'))
        conn.execute(insert(Pacient).values(id_pacient=10, blood_type='B-'))
        conn.execute(insert(Pacient).values(id_pacient=11, blood_type='B-'))
        conn.execute(insert(Pacient).values(id_pacient=12, blood_type='B-'))
        conn.commit()
    
    # 17 - Quantidade de doadores por tipo sanguíneo
    def pacient_per_blood_type(self, session):
        result = session.execute(select(Pacient.blood_type, func.count(Pacient.id_pacient)).group_by(Pacient.blood_type))

        for i in result:
            print(f"Tipo sanguíneo: {i[0]}      Número de doadores: {i[1]}")