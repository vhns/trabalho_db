from models import Base, blood_storage, donation_center
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import INTEGER, VARCHAR, SMALLINT, ForeignKey, select, insert, func

class Storage(Base):
    __tablename__ = "storage"
    id_storage: Mapped [int] = mapped_column(INTEGER, nullable=False,primary_key=True, autoincrement=True)
    id_center: Mapped [int] = mapped_column(INTEGER, ForeignKey(donation_center.Donation_center.id_center, ondelete='SET NULL'), nullable=True)
    street: Mapped [str] = mapped_column(VARCHAR(100), nullable=False)
    s_number: Mapped [int] = mapped_column(SMALLINT, nullable=False)
    neighborhood: Mapped [str] = mapped_column(VARCHAR(45), nullable=False)

    blood_storage: Mapped ["Blood_storage"] = relationship("Blood_storage", backref="storage")

    def insert_storage(self, engine):
        conn = engine.connect()
        conn.execute(insert(Storage).values(id_storage=1, id_center=1, street='Avenida das torres',
                                            s_number=1,
                                            neighborhood='Jardim das americas'))
        conn.execute(insert(Storage).values(id_storage=2, id_center=2, street='Avenida das torres',
                                            s_number=8,
                                            neighborhood='Jardim das americas'))
        conn.execute(insert(Storage).values(id_storage=3, id_center=3, street='Avenida das torres',
                                            s_number=9,
                                            neighborhood='Jardim das americas'))
        conn.execute(insert(Storage).values(id_storage=4, id_center=4, street='Avenida das torres',
                                            s_number=10,
                                            neighborhood='Jardim das americas'))
        conn.execute(insert(Storage).values(id_storage=5, id_center=5, street='Avenida das torres',
                                            s_number=11,
                                            neighborhood='Jardim das americas'))
        conn.execute(insert(Storage).values(id_storage=6, id_center=6, street='Avenida das torres',
                                            s_number=12,
                                            neighborhood='Jardim das americas'))
        conn.commit()

    # 10 - Espaço livre no estoque
    def free_space_storage(self, session):
        result = session.execute(select(func.count(Storage.id_storage)).where(Storage.id_storage != blood_storage.Blood_storage.id_storage))

        for i in result:
            print(f"Espaço livre: {i[0]}")
    
    # 11 - Espaço ocupado no estoque
    def occupied_space_storage(self, session):
        result = session.execute(select(func.count(Storage.id_storage)))

        for i in result:
            print(f"Espaço ocupado: {i[0]}")