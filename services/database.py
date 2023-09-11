from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from urllib.parse import quote

instance = f"mysql+pymysql://car_rental:{quote('car_rental')}@localhost:3306/car_rental"

if not database_exists(url=instance):
    create_database(url=instance)

engine = create_engine(url=instance, echo=True)
session = Session(bind=engine, autoflush=True, autocommit=False)
