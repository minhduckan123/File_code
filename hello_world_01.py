import sqlite3
import os
from hello_world_02 import drop_table_queries, create_table_queries

DATABASE_FILE = "sparkify.db"

con = None


def create_database():
    if os.path.isfile(DATABASE_FILE):
        os.unlink(DATABASE_FILE)

    connect = sqlite3.connect(DATABASE_FILE)
    cursor = connect.cursor()
    print("Created DB")

    return cursor, connect


def drop_tables(cursor, connect):
    for query in drop_table_queries:
        cursor.execute(query)
        connect.commit()
    print("Dropped DB")


def creat_tables(cursor, connect):
    for query in create_table_queries:
        cursor.execute(query)
        connect.commit()
    print("Created tables")


def main():
    cursor, connect = create_database()

    #     drop_tables(cursor, connect)

    creat_tables(cursor, connect)
    connect.close()


main()
