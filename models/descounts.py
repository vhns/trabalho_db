from models import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import INTEGER, VARCHAR, DECIMAL, insert

class Descount(Base):
    __tablename__ = "descount"
    id_descount: Mapped [int] = mapped_column (INTEGER, nullable=False, primary_key=True, autoincrement=True)
    descount_value: Mapped [float] = mapped_column (DECIMAL(6,2), nullable=False)
    descount_description: Mapped [str] = mapped_column (VARCHAR(45), nullable=False)

    payment_descounts: Mapped["Payment_descounts"] = relationship("Payment_descounts", backref="descounts")

    def insert_descount(self, engine):
        conn = engine.connect()
        conn.execute(insert(Descount).values(id_descount=1, descount_value=100.00, descount_description='Desconto 1'))
        conn.execute(insert(Descount).values(id_descount=2, descount_value=10.00, descount_description='Desconto 2'))
        conn.execute(insert(Descount).values(id_descount=3, descount_value=100.00, descount_description='Desconto 3'))
        conn.execute(insert(Descount).values(id_descount=4, descount_value=100.00, descount_description='Desconto 4'))
        conn.execute(insert(Descount).values(id_descount=5, descount_value=100.00, descount_description='Desconto 5'))
        conn.execute(insert(Descount).values(id_descount=6, descount_value=100.00, descount_description='Desconto 6'))
        conn.commit()