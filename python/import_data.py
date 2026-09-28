from pathlib import Path
import sqlite3

# __file__ - is not the directory Python is currently running from. It is the location of the Python script itself.
# .resolve() cleans the absolute location
# .parent -> python/
# .parent -> retail-sales-analysis/
project_root = Path(__file__).resolve().parent.parent
print(project_root)

# project_root gives the absolute path to the project's root folder

# the rest of the path to the database
database_path = project_root / "data" / "retail_sales.db"

print(database_path) # print the path that you have added
print(database_path.is_file()) # checks whether a file exists at that location.

# connect to the data base
connection = sqlite3.connect(database_path)
# -----------------------------------------------

# A cursor is what Python uses to actually send SQL instructions through that connection.
# Think of it like Python has opened the door to SQLite
cursor = connection.cursor()

# cursor can execute SQL - have to send it as a string
cursor.execute("""
    SELECT name 
    FROM sqlite_master
    WHERE type = 'table';
""")

# Give me all rows returned by the query. Then store the result in a variable
tables = cursor.fetchall()
print(tables)
# ------------------------------------------------
connection.close()