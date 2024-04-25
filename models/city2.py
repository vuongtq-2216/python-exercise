from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import db.connection as con


Base = declarative_base()

class City2(Base):
    __tablename__ = 'cities2'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    population = Column(Integer)

    def __repr__(self):
        return f"<City2(name='{self.name}', population={self.population})>"
# Base.metadata.create_all(con.engine)
