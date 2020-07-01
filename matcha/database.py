#!/usr/bin/python


import sqlite3

DATABASE = 'database.db'

def connect_db():
    return sqlite3.connect(DATABASE)

def run_sql_script(filename, connection):
    file = open(filename, 'r')
    sql = s = " ".join(file.readlines())

    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("DATABASE POPULATED!")


def main():
    db = connect_db()
    run_sql_script("populate_db.sql", db)


if __name__ == "__main__":
    main()