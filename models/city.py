from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True)
    city = Column(String(255))
    country = Column(String(255))
    capital = Column(String(255))
    population = Column(Integer)

    def __repr__(self):
        return f"<City(name='{self.name}', population={self.population})>"
