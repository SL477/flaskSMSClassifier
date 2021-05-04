import sqlite3
from sqlite3 import Error
import json
import pandas as pd

def sql_connection():
    """
    This is to get the database connection
    """
    try:
        return sqlite3.connect('data.db')
    except Error:
        print(Error)

def executeSql(con, sqlText):
    """
    This is to execute arbitary SQL commands
    """
    cursor = con.cursor()
    cursor.execute(sqlText)
    con.commit()

def firstTimeSetup():
    """
    This is to run the first time setups

    messages
    Columns:
    id
    msg
    type

    types
    Columns:
    id
    desc
    """
    con = sql_connection()
    messageTableSql = "CREATE TABLE messages(id integer PRIMARY KEY, msg text, type integer);"
    executeSql(con, "DROP TABLE IF EXISTS messages;")
    executeSql(con, messageTableSql)
    typesTableSql = "CREATE TABLE types(id bit, desc text);"
    executeSql(con, "DROP TABLE IF EXISTS types;")
    executeSql(con, typesTableSql)

    typesRowsSQL = "INSERT INTO types (id, desc) VALUES (0, 'spam'), (1,'ham')"
    executeSql(con, typesRowsSQL)
    con.close()

def insertDataIntoMessages(con, msgString, typeBool):
    """
    This is to insert a line of data into the messages table with its classification
    """
    cursor = con.cursor()
    cursor.execute("INSERT INTO messages (msg, type) VALUES (?,?)", (msgString, typeBool))
    con.commit()

def getAllData():
    """
    Get all of the data from the database
    """
    with sql_connection() as con:
        cursor = con.cursor()
        cursor.execute("SELECT msg.id, msg.msg, msg.type, t.desc FROM messages msg JOIN types t ON msg.type = t.id")
        data = cursor.fetchall()
        return json.dumps(data)

def getMessageTableDataFrame():
    """
    Get the messages table as a DataFrame
    """
    con = sql_connection()
    df = pd.read_sql("SELECT msg, type FROM messages", con)
    con.close()
    return df