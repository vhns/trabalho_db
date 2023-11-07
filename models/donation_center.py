from models import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import INTEGER, VARCHAR, SMALLINT, TIME, insert, update, delete
from datetime import time

class Donation_center(Base):
    __tablename__ = "donation_center"
    id_center: Mapped [int] = mapped_column(INTEGER, nullable=False, primary_key=True, autoincrement=True)
    center_name: Mapped [str] = mapped_column(VARCHAR(45), nullable=False)
    street: Mapped [str] = mapped_column(VARCHAR(100), nullable=False)
    s_number: Mapped [int] = mapped_column(INTEGER, nullable=False)
    neighborhood: Mapped [str] = mapped_column(VARCHAR(45), nullable=False)
    working_period_s: Mapped [time] = mapped_column(TIME, nullable=False)
    working_period_e: Mapped [time] = mapped_column(TIME, nullable=False)

    employee: Mapped ["Employee"] = relationship("Employee", backref="donation_center", cascade='all, delete-orphan')
    storage: Mapped ["Storage"] = relationship("Storage", backref="donation_center", cascade='all, delete-orphan')
    pacient_center: Mapped ["Pacient_center"] = relationship("Pacient_center", backref="donation_center", cascade='all, delete-orphan')
    receiver_center: Mapped ["Receiver_center"] = relationship("Receiver_center", backref="donation_center", cascade='all, delete-orphan')

    def insert_center(self, engine):
        conn = engine.connect()
        conn.execute(insert(Donation_center).values(id_center=1,
                                                    center_name='Centro de doação 1',
                                                    street='Avenida das torres',
                                                    s_number=2,
                                                    neighborhood='Jardim das Americas',
                                                    working_period_s='08:00:00',
                                                    working_period_e='18:00:00'))
        conn.execute(insert(Donation_center).values(id_center=2,
                                                    center_name='Centro de doação 2',
                                                    street='Avenida das torres',
                                                    s_number=3,
                                                    neighborhood='Jardim das Americas',
                                                    working_period_s='08:00:00',
                                                    working_period_e='18:00:00'))
        conn.execute(insert(Donation_center).values(id_center=3,
                                                    center_name='Centro de doação 3',
                                                    street='Avenida das torres',
                                                    s_number=4,
                                                    neighborhood='Jardim das Americas',
                                                    working_period_s='08:00:00',
                                                    working_period_e='18:00:00'))
        conn.execute(insert(Donation_center).values(id_center=4,
                                                    center_name='Centro de doação 4',
                                                    street='Avenida das torres',
                                                    s_number=5,
                                                    neighborhood='Jardim das Americas',
                                                    working_period_s='08:00:00',
                                                    working_period_e='18:00:00'))
        conn.execute(insert(Donation_center).values(id_center=5,
                                                    center_name='Centro de doação 5',
                                                    street='Avenida das torres',
                                                    s_number=6,
                                                    neighborhood='Jardim das Americas',
                                                    working_period_s='08:00:00',
                                                    working_period_e='18:00:00'))
        conn.execute(insert(Donation_center).values(id_center=6,
                                                    center_name='Centro de doação 6',
                                                    street='Avenida das torres',
                                                    s_number=7,
                                                    neighborhood='Jardim das Americas',
                                                    working_period_s='08:00:00',
                                                    working_period_e='18:00:00'))
        conn.commit()

    def update_donation_center(self, engine):
        conn = engine.connect()
        conn.execute(update(Donation_center).where(Donation_center.id_center == 5).values(neighborhood='Bacacheri'))
        conn.execute(update(Donation_center).where(Donation_center.id_center == 5).values(street='Rua Nicarágua'))
        conn.commit()
    
    def delete_donation_center(self, engine):
        conn = engine.connect()
        conn.execute(delete(Donation_center).where(Donation_center.id_center == 2))
        conn.commit()