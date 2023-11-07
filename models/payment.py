from models import Base, Employee
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import INTEGER, ForeignKey, DATETIME, DECIMAL, select, insert, delete, func
from datetime import date

class Payment(Base):
    __tablename__ = "payment"
    id_payment: Mapped [int] = mapped_column (INTEGER, nullable=False, primary_key=True, autoincrement=True)
    id_employee: Mapped [int] = mapped_column (INTEGER, ForeignKey(Employee.id_employee, ondelete='CASCADE'), nullable=False)
    payment_value: Mapped [float] = mapped_column (DECIMAL(6,2), nullable=False)
    payment_date: Mapped [date] = mapped_column (DATETIME, nullable=False, default=func.NOW())
    
    payment_descounts: Mapped["Payment_descounts"] = relationship("Payment_descounts", backref="payment", cascade='all, delete-orphan')

    def insert_payment(self, engine):
        conn = engine.connect()
        conn.execute(insert(Payment).values(id_employee=1, payment_value=1000.00))
        conn.execute(insert(Payment).values(id_employee=2, payment_value=2000.00))
        conn.execute(insert(Payment).values(id_employee=3, payment_value=3000.00))
        conn.execute(insert(Payment).values(id_employee=4, payment_value=4000.00))
        conn.execute(insert(Payment).values(id_employee=5, payment_value=5000.00))
        conn.execute(insert(Payment).values(id_employee=6, payment_value=6000.00))
        conn.commit()
    
    def delete_payment(self, engine):
        conn = engine.connect()
        conn.execute(delete(Payment).where(Payment.id_payment==1))
        conn.commit()

     # 6 - Valor total de salário mensal
    def total_month_salary(self, session):
        result = session.execute(select(func.sum(Payment.payment_value)).where(func.month(Payment.payment_date) == func.month(func.current_date())))

        for i in result:
            print(f"Valor total de salário mensal: {i[0]}")

    # 7 - valor total de salário anual
    def total_year_salary(self, session):
        result = session.execute(select(func.sum(Payment.payment_value)).where(func.year(Payment.payment_date) == func.year(func.current_date())))

        for i in result:
            print(f"Valor total de salário anual: {i[0]}")

    # 19 - Média de salário por tipo de funcionário
    def average_payment_per_type_employee(self, session):
        result = session.execute(select(Employee.e_function, func.avg(Payment.payment_value)).join(Employee, Payment.id_employee == Employee.id_employee).group_by(Employee.e_function))

        for i in result:
            print(f"Função do funcionário: {i[0]}       Salário médio: {i[1]}")