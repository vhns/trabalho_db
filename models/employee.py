from models import Base, person, donation_center
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import INTEGER, VARCHAR, ForeignKey, TIME, select, insert, update, func
from datetime import time

class Employee(Base):
    __tablename__ = "employee"
    id_employee: Mapped [int] = mapped_column (INTEGER, ForeignKey(person.Person.id_person), primary_key=True)
    id_donation_center: Mapped [int] = mapped_column (INTEGER, ForeignKey(donation_center.Donation_center.id_center, ondelete='SET NULL'), nullable=True,)
    e_function: Mapped [str] = mapped_column (VARCHAR(45), nullable=False)
    work_time_s: Mapped [time] = mapped_column (TIME, nullable=False)
    work_time_e: Mapped [time] = mapped_column (TIME, nullable=False)

    payment: Mapped ["Payment"] = relationship("Payment", backref="employee")
    blood_bags: Mapped ["Blood_bags"] = relationship("Blood_bags", backref="employee")

    def insert_employee(self, engine):
        conn = engine.connect()
        conn.execute(insert(Employee).values(id_employee=1, id_donation_center=1, e_function='Limpeza', work_time_s='08:00:00', work_time_e='18:00:00'))
        conn.execute(insert(Employee).values(id_employee=2, id_donation_center=2, e_function='Coleta', work_time_s='08:00:00', work_time_e='18:00:00'))
        conn.execute(insert(Employee).values(id_employee=3, id_donation_center=3, e_function='Administrativo', work_time_s='08:00:00', work_time_e='18:00:00'))
        conn.execute(insert(Employee).values(id_employee=4, id_donation_center=4, e_function='Limpeza', work_time_s='08:00:00', work_time_e='18:00:00'))
        conn.execute(insert(Employee).values(id_employee=5, id_donation_center=5, e_function='Coleta', work_time_s='08:00:00', work_time_e='18:00:00'))
        conn.execute(insert(Employee).values(id_employee=6, id_donation_center=1, e_function='Coleta', work_time_s='08:00:00', work_time_e='18:00:00'))
        conn.commit()

    def update_employee(self, engine):
        conn = engine.connect()
        conn.execute(update(Employee).where(Employee.id_employee == 1).values(e_function='Administrativo'))
        conn.commit()

    # 8 - Número total de funcioários
    def total_employees(self, session):
        result = session.execute(select(func.count(Employee.id_employee)))

        for i in result:
            print(f"Número total de funcionários: {i[0]}")

    # 16 - Quantidade de funcionarios por centro de doação
    def total_employees_per_center(self, session):
        result = session.query(Employee.id_donation_center, func.count(Employee.id_employee)).select_from(Employee).group_by(Employee.id_donation_center).all()
        print(result)
