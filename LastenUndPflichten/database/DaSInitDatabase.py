import sqlite3

from pathlib import Path


def init_db(db_name:str, db_schema_file_name:str):

    database_con = sqlite3.connect(db_name)

    # read schema script file
    db_schema_file = open(db_schema_file_name, 'r')

    # execute script
    database_con.cursor().executescript(db_schema_file.read())
    database_con.commit()

 
# create database 

database_name = input("Name der Datenbank:")
database_schema_name = input("Name des Datenbankschemas:")

if database_name == "":
    database_name = "DaS.db"

if database_schema_name == "":
    database_schema_name = "schema.sql"

database_file = Path(database_name)
database_file.touch(exist_ok=True)

init_db(database_name, database_schema_name)