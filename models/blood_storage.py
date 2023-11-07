from models import Base, blood_bags, storage
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import INTEGER, ForeignKey, select, insert, func

class Blood_storage(Base):
    __tablename__ = "blood_storage"
    id_bags: Mapped [int] = mapped_column(INTEGER, ForeignKey(blood_bags.Blood_bags.id_bags, ondelete='CASCADE'), nullable=False, primary_key=True)
    id_storage : Mapped [int] = mapped_column(INTEGER, ForeignKey(storage.Storage.id_storage), nullable=False)

    def insert_blood_storage(self, engine):
        conn = engine.connect()
        conn.execute(insert(Blood_storage).values(id_bags=1, id_storage=2))
        conn.execute(insert(Blood_storage).values(id_bags=2, id_storage=5))
        conn.execute(insert(Blood_storage).values(id_bags=3, id_storage=1))
        conn.execute(insert(Blood_storage).values(id_bags=4, id_storage=2))
        conn.execute(insert(Blood_storage).values(id_bags=5, id_storage=5))
        conn.execute(insert(Blood_storage).values(id_bags=6, id_storage=1))
        conn.commit()

    # 13 -  Quantidade de bolsas que sairam por centro de doação
    def departured_bb_per_center(self, session):
        result = session.execute(select(storage.Storage.id_center, func.count(Blood_storage.id_bags)).join(storage.Storage, Blood_storage.id_storage == storage.Storage.id_storage).group_by(storage.Storage.id_center))

        for i in result:
            print(f"Centro de doação: {i[0]}        Número de bolsas de sangue por centro de doação: {i[1]}")
