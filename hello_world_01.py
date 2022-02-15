import sqlite3
import os
from hello_world_02 import drop_table_queries,create_table_queries

con = None

def create_database():
    
    try:
        os.remove("sparkify.db")
    except:
        pass
    
    con = sqlite3.connect("sparkify.db")
    cur = con.cursor()
    
    return cur, con
    

def drop_tables(cur, con):
    for query in drop_table_queries:
        cur.execute(query)
        con.commit()
        
def creat_tables(cur, con):
    for query in create_table_queries:
        cur.execute(query)
        con.commit()


def main():
    cur, con = create_database()
    
    try:
        drop_tables(cur,con)
    except:
        pass
    
    creat_tables(cur, con)
    con.close()
    
main()    
