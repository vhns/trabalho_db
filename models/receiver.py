from datetime import date
from models import Base, person
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import INTEGER, ForeignKey, DATETIME, Date, insert, delete, cast, func
from datetime import date


class Receiver(Base):
    __tablename__ = "receiver"
    id_receiver: Mapped [int] = mapped_column (INTEGER, ForeignKey(person.Person.id_person, ondelete='CASCADE'), nullable=False, primary_key=True)
    date_recieve: Mapped [date] = mapped_column (DATETIME, nullable=True)

    receiver_center: Mapped ["Receiver_center"] = relationship("Receiver_center", backref="receiver")
    blood_bags: Mapped['Blood_bags'] = relationship('Blood_bags', backref='receiver')

    def insert_receiver(self, engine):
        conn = engine.connect()
        conn.execute(insert(Receiver).values(id_receiver=13, 
                                            date_recieve=func.NOW()))
        conn.execute(insert(Receiver).values(id_receiver=14, 
                                            date_recieve=func.NOW()))
        conn.execute(insert(Receiver).values(id_receiver=15, 
                                            date_recieve=func.NOW()))
        conn.execute(insert(Receiver).values(id_receiver=16, 
                                            date_recieve=func.NOW()))
        conn.execute(insert(Receiver).values(id_receiver=17, 
                                            date_recieve=func.NOW()))
        conn.execute(insert(Receiver).values(id_receiver=18, 
                                            date_recieve=func.NOW()))
        conn.commit()
    
    def delete_receiver(self, engine):
        conn = engine.connect()
        conn.execute(delete(Receiver).where(Receiver.id_receiver == 13))
        conn.commit()


