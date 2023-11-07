from datetime import timedelta, datetime
from models import Base, pacient, employee, receiver
from sqlalchemy.orm import Mapped, mapped_column, relationship, aliased
from sqlalchemy import INTEGER, VARCHAR, DATETIME, ForeignKey, select, insert, delete, func
from datetime import datetime

class Blood_bags (Base):
    __tablename__ = "blood_bags"
    id_bags: Mapped [int] = mapped_column(INTEGER, nullable=False, primary_key=True, autoincrement=True)
    id_receiver: Mapped [int] = mapped_column(INTEGER, ForeignKey(receiver.Receiver.id_receiver, ondelete='SET NULL'), nullable=True)
    id_employee: Mapped [int] = mapped_column(INTEGER, ForeignKey(employee.Employee.id_employee), nullable=False)
    id_pacient: Mapped [int] = mapped_column(INTEGER, ForeignKey(pacient.Pacient.id_pacient), nullable=False)
    blood_type: Mapped [str] = mapped_column(VARCHAR(3), nullable=False)
    entry_date: Mapped [datetime] = mapped_column(DATETIME, nullable=False, default=func.NOW())
    departure_date:  Mapped [datetime] = mapped_column(DATETIME, nullable=True) 

    blood_storage: Mapped ["Blood_storage"] = relationship("Blood_storage", backref="blood_bags", cascade='all, delete-orphan')

    def insert_blood_bags(self, engine):
        conn = engine.connect()
        conn.execute(insert(Blood_bags).values( id_receiver = 13,
                                                id_employee=2,
                                                id_pacient=7,
                                                blood_type='B-',
                                                departure_date=func.NOW()))
        conn.execute(insert(Blood_bags).values(id_receiver=14,
                                                id_employee=5,
                                                id_pacient=8,
                                                blood_type='B-',
                                                departure_date=func.NOW()))
        conn.execute(insert(Blood_bags).values(id_receiver=15,
                                                id_employee=6,
                                                id_pacient=9,
                                                blood_type='B-',
                                                departure_date=func.NOW()))
        conn.execute(insert(Blood_bags).values(id_receiver=16,
                                                id_employee=2,
                                                id_pacient=10,
                                                blood_type='B-',
                                                departure_date=func.NOW()))
        conn.execute(insert(Blood_bags).values(id_receiver=17,
                                                id_employee=5,
                                                id_pacient=11,
                                                blood_type='B-',
                                                departure_date=func.NOW()))
        conn.execute(insert(Blood_bags).values(id_receiver=17,
                                                id_employee=6,
                                                id_pacient=12,
                                                blood_type='B-',
                                                departure_date=func.NOW()))
        
        conn.commit()

    def delete_blood_bags(self, engine):
        conn = engine.connect()
        conn.execute(delete(Blood_bags).where(Blood_bags.id_bags == 2))
        conn.commit()

    # 1 - Quantidade de pacientes por mês/dia/ano
    def total_pacients_per_dmy(self, session):
        day = func.day(Blood_bags.entry_date)
        month = func.month(Blood_bags.entry_date)
        year = func.year(Blood_bags.entry_date)

        result = session.execute(select(func.count(Blood_bags.id_pacient), day, month, year).group_by(year, month, day))

        for i in result:
            print(f"Número de pacientes: {i[0]}     Dia: {i[1]}/{i[2]}/{i[3]}")


    # 2 - Número total de bolsas de sangue
    def total_bb(self, session):
        result = session.execute(select(func.count(Blood_bags.id_bags)))

        for i in result:
            print(f"Número total de bolsas de sangue: {i[0]}")


    # 3 - Número de bolsas de sangue por tipo sanguineo
    def total_bb_per_type(self, session):
        result = session.execute(select(Blood_bags.blood_type, func.count(Blood_bags.id_bags)).group_by(Blood_bags.blood_type))

        for i in result:
            print(f"Tipo sanguíneo: {i[0]}      Total: {i[1]}")

    
    # 4 - Quantidade de bolsas que expiram no mês seguinte
    def expiring_bb(self, session):
        result = session.execute(select(func.count(Blood_bags.id_bags)).where(func.month(Blood_bags.departure_date) == func.month(func.current_date()) + 1))

        for i in result:
            print(f"Número de bolsas que expiram no próximo mês: {i[0]}")


    # 5 - Quantidade de bolsas que expiram no mês seguinte por tipo sanguineo
    def expiring_bb_per_type(self, session):
        result = session.execute(select(Blood_bags.blood_type, func.count(Blood_bags.id_bags)).where(func.month(Blood_bags.departure_date) == func.month(func.current_date()) + 1).group_by(Blood_bags.blood_type))

        for i in result:
            print(f"Tipo sanguíneo: {i[0]}      Número de bolsas de sangue que expiram no próximo mês: {i[1]}")

    # 14 - Quantidade em litros de sangue
    def total_liters_bb(self, session):
        result = session.execute(select(func.count(Blood_bags.id_bags)*0.65))

        for i in result:
            print(f"Volume total em litros de sangue: {i[0]}")

    # 15 - Quantidade em litros de sangue por tipo sanguineo
    def total_liters_bb_per_type(self, session):
        result = session.execute(select(Blood_bags.blood_type, func.count(Blood_bags.id_bags)*0.65).group_by(Blood_bags.blood_type))

        for i in result:
            print(f"Tipo sanguíneo: {i[0]}      Volume total em litros de sangue: {i[1]}")

    # 16 - Média de bolsas de sangue por paciente
    def average_bb_per_pacient(self, session):
        inner_stmt = select(func.count(Blood_bags.id_bags).label('num_bags')).group_by(Blood_bags.id_pacient)
        subq = inner_stmt.subquery()

        result = session.query(func.avg(subq.c.num_bags))

        for i in result:
            print(f"Média de bolsas por paciente: {i[0]}")
    
    # 18 - Número de bolsas por ano e tipo sanguíneo:
    def bb_per_year_and_type(self, session):
        result = session.execute(select(func.year(Blood_bags.entry_date), Blood_bags.blood_type, func.count(Blood_bags.id_bags)).group_by(func.year(Blood_bags.entry_date), Blood_bags.blood_type))

        for i in result:
            print(f"Ano: {i[0]}         Tipo sanguíneo: {i[1]}          Número de bolsas de sangue: {i[2]}")
