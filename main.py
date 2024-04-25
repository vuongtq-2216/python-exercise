from db.connection import DatabaseManager
import pdb;
import csv
import operator
from sqlalchemy.orm import declarative_base

from models.city import City

Base = declarative_base()

def init_db():
  db_manager = DatabaseManager()
  db_manager.create_database_if_not_exists()
  db_manager.create_tables()
  return db_manager.create_session()

def read_csv_to_dicts(path):
  with open(path, encoding="utf8") as f:
    csv_reader = csv.DictReader(f)

    data = [
      {
        "city": row["city"],
        "country": row["country"],
        "capital": row["capital"],
        "population": int(float(row["population"])) if row["population"] else 0
      }
      for row in csv_reader
    ]
  return data

def insert_data_to_db(session, data):
  try:
    session.bulk_insert_mappings(City, data)
    session.commit()
    print("Data has been successfully inserted.")
  except Exception as e:
    session.rollback()
    print(f"Error: {e}")
  finally:
    session.close()

def main():
  CSV_PATH = "./worldcities.csv"

  session = init_db()
  data = read_csv_to_dicts(CSV_PATH)
  insert_data_to_db(session, data)


  # update city population
  city = session.query(City).filter(City.city == "London").first()
  city.population = 1000000
  session.commit()

  # delete city
  city = session.query(City).filter(City.city == "London").first()
  session.delete(city)
  session.commit()

  # list cities
  cities = session.query(City).order_by(City.population.desc()).limit(10).all()
  for city in cities:
    print(city.city, city.country, city.capital, city.population)

if __name__ == "__main__":
  main()
