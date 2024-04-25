import os
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
from models import *
# from ModelBase import Base
from models.city import City

# from models import Base

load_dotenv()

Base = declarative_base()

class DatabaseManager:
  def __init__(self):
    db_connection_string = os.getenv('DB_CONNECTION')
    self.engine = create_engine(db_connection_string, echo=True)
    self.Session = sessionmaker(bind=self.engine)

  def create_database_if_not_exists(self):
    if not database_exists(self.engine.url):
      create_database(self.engine.url)

  def create_tables(self):
    Base.metadata.create_all(self.engine, tables=[City.__table__])
  # def create_tables(self):
  #     Base.metadata.create_all(self.engine)

  def create_session(self):
    return self.Session()
