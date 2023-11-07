from models import Base, Receiver, Donation_center
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import INTEGER, ForeignKey, insert, select, func

class Receiver_center(Base):
    __tablename__ = "receiver_center"
    id_receiver: Mapped [int] = mapped_column(INTEGER, ForeignKey(Receiver.id_receiver, ondelete='CASCADE'), nullable=False, primary_key=True)
    id_center: Mapped [int] = mapped_column(INTEGER, ForeignKey(Donation_center.id_center, ondelete='CASCADE'), nullable=False)

    def insert_receiver_center(self, engine):
        conn = engine.connect()
        conn.execute(insert(Receiver_center).values(id_receiver=13 , id_center=2))
        conn.execute(insert(Receiver_center).values(id_receiver=14 , id_center=5))
        conn.execute(insert(Receiver_center).values(id_receiver=15 , id_center=1))
        conn.execute(insert(Receiver_center).values(id_receiver=16 , id_center=2))
        conn.execute(insert(Receiver_center).values(id_receiver=17 , id_center=5))
        conn.execute(insert(Receiver_center).values(id_receiver=18 , id_center=1))
        conn.commit()
    
    # 20 - Número de recebedores por centro de doação
    def total_receiver_per_center(self, session):
        result = session.execute(select(Receiver_center.id_center, func.count(Receiver_center.id_receiver)).group_by(Receiver_center.id_center))

        for i in result:
            print(f"Centro de doação: {i[0]}        Número de recebedores: {i[1]}")