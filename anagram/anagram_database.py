"""
Program: anagram_database.py
Author: Rachel LI
Last date modified: 31/07/2020

The purpose of this program is to use query to read database
"""
import sqlite3
from sqlite3 import Error

def create_connection(db):
    """Connect to SQLite database
    :param db: filename of database
    :return: connection if no error, otherwise None
    """
    try:
        conn = sqlite3.connect(db)
        return conn
    except Error as err:
        print(err)
    return None

def create_table(conn, table_sql):
    """Create table with SQL statement"""
    try:
        c = conn.cursor()
        c.execute(table_sql)
    except Error as err:
        print(err)

def create_tables(db):
    """Use database connection to create anagram table
    :param db: database object
    :return: return tables in database
    """
    sql_create_anagram_table = """ CREATE TABLE IF NOT EXISTS anagram (
                                    anagram TEXT NOT NULL,
                                    word TEXT NOT NULL
                                    ); """
    conn = create_connection(db)
    if conn is not None:
        #create table
        create_table(conn, sql_create_anagram_table)
    else:
        print("Unable to connect to " + str(db))

def create_anagram(conn, anagram):
    """ Create new anagram for table
    :param anagram:
    :return: anagram id
    """
    sql = """ INSERT INTO anagram(anagram, word)
              VALUES(?,?); """
    c = conn.cursor() #cursor object
    c.execute(sql, anagram)
    return c.lastrowid #return the row id of cursor object

def select_all_anagrams(conn):
    """ Query all rows of anagram table
    :param conn: connection object
    :return: rows
    """
    c = conn.cursor()
    c.execute("SELECT * FROM anagram;")
    rows = c.fetchall()
    return rows

