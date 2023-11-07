from models import Base, Blood_bags, pacient, donation_center
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import INTEGER, ForeignKey, select, insert, func

class Pacient_center(Base):
    __tablename__ = "pacient_center"
    id_pacient: Mapped [int] = mapped_column(INTEGER, ForeignKey(pacient.Pacient.id_pacient), nullable=False, primary_key=True)
    id_center: Mapped [int] = mapped_column(INTEGER, ForeignKey(donation_center.Donation_center.id_center, ondelete='CASCADE'), nullable=False)

    def insert_pacient_center(self, engine):
        conn = engine.connect()
        conn.execute(insert(Pacient_center).values(id_pacient=7, id_center=2))
        conn.execute(insert(Pacient_center).values(id_pacient=8, id_center=5))
        conn.execute(insert(Pacient_center).values(id_pacient=9, id_center=1))
        conn.execute(insert(Pacient_center).values(id_pacient=10, id_center=2))
        conn.execute(insert(Pacient_center).values(id_pacient=11, id_center=5))
        conn.execute(insert(Pacient_center).values(id_pacient=12, id_center=1))
        conn.commit()

    # 12 - Quantidade de pacientes atendidos por centro de doação
    def total_pacient_per_center(self, session):
        result = session.execute(select(Pacient_center.id_center, func.count(Blood_bags.id_pacient)).join(Blood_bags, Pacient_center.id_pacient == Blood_bags.id_pacient).group_by(Pacient_center.id_center))

        for i in result:
            print(f"Centro de doação: {i[0]}        Número de pacientes atendidos: {i[1]}")