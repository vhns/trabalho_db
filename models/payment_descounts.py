from models import Base, Payment, descounts
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import INTEGER, ForeignKey, insert

class Payment_descounts(Base):
    __tablename__ = "payment_descounts"
    id: Mapped[int] = mapped_column(INTEGER, primary_key=True, autoincrement=True)
    id_payment: Mapped [int] = mapped_column (INTEGER, ForeignKey(Payment.id_payment, ondelete='CASCADE') ,nullable=False)
    id_descount: Mapped [int] = mapped_column (INTEGER, ForeignKey(descounts.Descount.id_descount), nullable=False)

    def insert_payment_desconts(self, engine):
        conn = engine.connect()
        conn.execute(insert(Payment_descounts).values(id_payment=1, id_descount=6))
        conn.execute(insert(Payment_descounts).values(id_payment=2, id_descount=5))
        conn.execute(insert(Payment_descounts).values(id_payment=3, id_descount=4))
        conn.execute(insert(Payment_descounts).values(id_payment=4, id_descount=3))
        conn.execute(insert(Payment_descounts).values(id_payment=5, id_descount=2))
        conn.execute(insert(Payment_descounts).values(id_payment=6, id_descount=1))
        conn.commit()