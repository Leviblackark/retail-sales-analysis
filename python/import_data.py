from pathlib import Path
import sqlite3
import pandas as pd

# __file__ - is not the directory Python is currently running from. It is the location of the Python script itself.
# .resolve() cleans the absolute location
# .parent -> python/
# .parent -> retail-sales-analysis/
project_root = Path(__file__).resolve().parent.parent
print(f"Location of python script: {project_root}\n")

# project_root gives the absolute path to the project's root folder

# the rest of the path to the database
database_path = project_root / "data" / "retail_sales.db"

print(f"Location of the database: {database_path}\n") # print the path that you have added
print(f"Does the file database exist as this location: {database_path.is_file()}\n") # checks whether a file exists at that location.

# -----------------------------------------------
# connect to the data base
connection = sqlite3.connect(database_path)

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
print(f"{tables}\n")
# ------------------------------------------------

# find the csv file 
csv_path = project_root / "data" / "processed" / "Coffee Shop Sales.csv"

print(f"CSV PATH: {csv_path}\n")
print(f"File exists at this location: {csv_path.is_file()}\n")

# read the csv into a pandas DataFrame
df = pd.read_csv(csv_path)
# display is different from jupyter notebook, have to wrap in a print
print(df.head(), "\n")


# Inspect the DataFrame
# Before we import anything into SQLite, we want to answer three basic questions:
# TODO: 1. How many rows and columns are in the full dataset?
# TODO: 2. What are all the column names?
# TODO: 3. What data type has pandas assigned to each column?

print(f"Shape: {df.shape}\n")
print(f"Column Names: {df.columns}\n")
print(f"what type has pandas assigned to each column:\n{df.dtypes}\n")

# Check for any missing values
print(df.isna().sum(), "\n")

# Check for duplicate transaction ID's
print(f"Count how many duplicated transaction_ids: {df["transaction_id"].duplicated().sum()}\n")

# -------------------------------------------------------------------------------------------
# append the dataframe into a existing 

# Safety check 
cursor.execute("""
    SELECT COUNT(*)
    FROM transactions;
""")

# expecting one result
row_count = cursor.fetchone()
print(row_count)

# only import when there is nothing inside transactions - Stops repeats
if row_count[0] == 0: 
    df.to_sql(
        name="transactions", # which table i'm loading into
        con=connection, # which existing Python variable holds the SQLite connection?
        if_exists="append", # keeps your existing table rather than replacing it.
        index=False, # don't add the pandas DataFrame index to SQLite
    )
else: 
    # do not import
    print("Data already exists")

# prove that it worked: 
cursor.execute("""
    SELECT COUNT(*)
    FROM transactions;
""")

updated_row_count = cursor.fetchone()
print(f"Check the row count after adding the data: {updated_row_count}")
print(f"df Row count {df.shape[0]}")
print(f"Row counts matchs: {updated_row_count[0] == df.shape[0]}")

print(df.head())
# ------------------------------------------------------------------------------------------
# Close the connection once your done with it 
connection.close()