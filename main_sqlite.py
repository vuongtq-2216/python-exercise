# main.py
import csv
import operator
import re
import sqlite3

CSV_PATH = "./city.csv"

if __name__=="__main__":

  with open(CSV_PATH, encoding="utf8") as f:

    csv_reader = csv.reader(f)
    cities = sorted(csv_reader, key=operator.itemgetter(1))

    try:
      con = sqlite3.connect("tutorial.db")
      cur = con.cursor()
      cur.execute("DROP TABLE IF EXISTS cities;")
      cur.execute("""CREATE TABLE cities(
        name TEXT NOT NULL,
        population INTEGER NOT NULL
      );""")
      cur.executemany("INSERT INTO cities(name, population) values (?,?)", cities)
      con.commit()
    except sqlite3.ProgrammingError as e:
      print("Error sqlite3")
    except Exception as e:
      # Rollback data
      print("Error .....")
    finally:
      con.close()
