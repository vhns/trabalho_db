from models import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import INTEGER, VARCHAR, DATE, SMALLINT, insert, update, delete
from datetime import date


class Person (Base):
    __tablename__ = "person"
    id_person: Mapped [int] = mapped_column (INTEGER, nullable=False, primary_key=True, autoincrement=True)
    person_name: Mapped [str] = mapped_column (VARCHAR(100), nullable=False)
    birth_year: Mapped [date] = mapped_column (DATE, nullable=False)
    street: Mapped [str] = mapped_column (VARCHAR(45), nullable=False)
    house_number: Mapped [int] = mapped_column (SMALLINT, nullable=False)
    neighborhood: Mapped [str] = mapped_column (VARCHAR(45), nullable=False)
    cpf: Mapped[str] = mapped_column (VARCHAR(11), nullable=False, unique=True)
    sex: Mapped[str] = mapped_column (VARCHAR(1), nullable=False)

    pacient: Mapped["Pacient"] = relationship("Pacient", backref="person", cascade='all, delete-orphan')
    receiver: Mapped["Receiver"] = relationship("Receiver", backref="person", cascade='all, delete-orphan')
    employee: Mapped["Employee"] = relationship("Employee", backref="person", cascade='all, delete-orphan')
    
    def insert_person(self, engine):
        conn = engine.connect()
        conn.execute(insert(Person).values(person_name="Marco",
                                            birth_year="2004-01-01",
                                            street="Rua dos palotinos",
                                            house_number="1",
                                            neighborhood="xaxim",
                                            cpf="11111111111",
                                            sex="m"))
        conn.execute(insert(Person).values(person_name="Joao",
                                            birth_year="2004-01-01",
                                            street="Rua dos palotinos",
                                            house_number="1",
                                            neighborhood="xaxim",
                                            cpf="22222222222",
                                            sex="m"))
        conn.execute(insert(Person).values(person_name="Vitor",
                                            birth_year="2004-01-01",
                                            street="Rua dos palotinos",
                                            house_number="1",
                                            neighborhood="xaxim",
                                            cpf="33333333333",
                                            sex="m"))
        conn.execute(insert(Person).values(person_name="Henrique",
                                            birth_year="2004-01-01",
                                            street="Rua dos palotinos",
                                            house_number="1",
                                            neighborhood="xaxim",
                                            cpf="44444444444",
                                            sex="m"))
        conn.execute(insert(Person).values(person_name="Antonio",
                                            birth_year="2004-01-01",
                                            street="Rua dos palotinos",
                                            house_number="1",
                                            neighborhood="xaxim",
                                            cpf="55555555555",
                                            sex="m"))
        conn.execute(insert(Person).values(person_name="Pedro",
                                            birth_year="2004-01-01",
                                            street="Rua dos palotinos",
                                            house_number="1",
                                            neighborhood="xaxim",
                                            cpf="66666666666",
                                            sex="m"))
        conn.execute(insert(Person).values(person_name="Davi",
                                            birth_year="2004-01-01",
                                            street="Rua dos palotinos",
                                            house_number="1",
                                            neighborhood="xaxim",
                                            cpf="77777777777",
                                            sex="m"))
        conn.execute(insert(Person).values(person_name="Gustavo",
                                            birth_year="2004-01-01",
                                            street="Rua dos palotinos",
                                            house_number="1",
                                            neighborhood="xaxim",
                                            cpf="88888888888",
                                            sex="m"))
        conn.execute(insert(Person).values(person_name="Cleber",
                                            birth_year="2004-01-01",
                                            street="Rua dos palotinos",
                                            house_number="1",
                                            neighborhood="xaxim",
                                            cpf="99999999999",
                                            sex="m"))
        conn.execute(insert(Person).values(person_name="Maycon",
                                            birth_year="2004-01-01",
                                            street="Rua dos palotinos",
                                            house_number="1",
                                            neighborhood="xaxim",
                                            cpf="12111111111",
                                            sex="m"))
        conn.execute(insert(Person).values(person_name="Elisa",
                                            birth_year="2004-01-01",
                                            street="Rua dos palotinos",
                                            house_number="1",
                                            neighborhood="xaxim",
                                            cpf="13111111111",
                                            sex="f"))
        conn.execute(insert(Person).values(person_name="Santin",
                                            birth_year="2004-01-01",
                                            street="Rua dos palotinos",
                                            house_number="1",
                                            neighborhood="xaxim",
                                            cpf="14111111111",
                                            sex="m"))
        conn.execute(insert(Person).values(person_name="pessoa13",
                                            birth_year="2004-01-01",
                                            street="Rua dos palotinos",
                                            house_number="1",
                                            neighborhood="xaxim",
                                            cpf="15111111111",
                                            sex="m"))
        conn.execute(insert(Person).values(person_name="pessoa14",
                                            birth_year="2004-01-01",
                                            street="Rua dos palotinos",
                                            house_number="1",
                                            neighborhood="xaxim",
                                            cpf="16111111111",
                                            sex="m"))
        conn.execute(insert(Person).values(person_name="pessoa15",
                                            birth_year="2004-01-01",
                                            street="Rua dos palotinos",
                                            house_number="1",
                                            neighborhood="xaxim",
                                            cpf="17111111111",
                                            sex="m"))
        conn.execute(insert(Person).values(person_name="pessoa16",
                                            birth_year="2004-01-01",
                                            street="Rua dos palotinos",
                                            house_number="1",
                                            neighborhood="xaxim",
                                            cpf="18111111111",
                                            sex="m"))
        conn.execute(insert(Person).values(person_name="pessoa17",
                                            birth_year="2004-01-01",
                                            street="Rua dos palotinos",
                                            house_number="1",
                                            neighborhood="xaxim",
                                            cpf="19111111111",
                                            sex="m"))
        conn.execute(insert(Person).values(person_name="pessoa18",
                                            birth_year="2004-01-01",
                                            street="Rua dos palotinos",
                                            house_number="1",
                                            neighborhood="xaxim",
                                            cpf="11211111111",
                                            sex="m"))
        conn.commit()

    def update_person(self, engine):
        conn = engine.connect()
        conn.execute(update(Person).where(Person.person_name == 'Marco').values(street='Rua Colombo'))
        conn.execute(update(Person).where(Person.person_name == 'Cleber').values(cpf='01234567812'))
        conn.commit()

    def delete_person(self, engine):
        conn = engine.connect()
        conn.execute(delete(Person).where(Person.id_person == 14))
        conn.commit()