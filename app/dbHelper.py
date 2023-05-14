"""This is to contain the various code to help with the database"""
import sqlite3
from sqlite3 import Error
import json
import pandas as pd


def sql_connection() -> sqlite3.Connection:
    """This is to get the database connection

    Returns
    -------
    sqlite3.Connection
        The connection to the database"""
    try:
        return sqlite3.connect('data.db')
    except Error:
        print(Error)


def executeSql(con: sqlite3.Connection, sqlText: str):
    """This is to execute arbitrary SQL commands

    Parameters
    ----------
    con: sqlite3.Connection
        The connection to the database

    sqlText: str
        The SQL command to execute"""
    cursor = con.cursor()
    cursor.execute(sqlText)
    con.commit()


def firstTimeSetup():
    """This is to run the first time setups

    messages Columns:
    - id
    - msg
    - type

    types Columns:
    - id
    - desc"""
    con = sql_connection()
    messageTableSql = "CREATE TABLE messages(id integer PRIMARY KEY,"
    messageTableSql += "msg text, type integer);"
    executeSql(con, "DROP TABLE IF EXISTS messages;")
    executeSql(con, messageTableSql)
    typesTableSql = "CREATE TABLE types(id bit, desc text);"
    executeSql(con, "DROP TABLE IF EXISTS types;")
    executeSql(con, typesTableSql)

    typesRowsSQL = "INSERT INTO types (id, desc) VALUES (0, 'spam'), (1,'ham')"
    executeSql(con, typesRowsSQL)
    con.close()


def insertDataIntoMessages(con: sqlite3.Connection, msgString: str,
                           typeBool: bool):
    """This is to insert a line of data into the messages table with its
    classification

    Parameters
    ----------
    con: sqlite3.Connection
        The database to connect to

    msgString: str
        The message to insert

    typeBool: bool
        The classification of the message"""
    cursor = con.cursor()
    cursor.execute("INSERT INTO messages (msg, type) VALUES (?,?)",
                   (msgString, typeBool))
    con.commit()


def getAllData() -> dict:
    """Get all of the data from the database

    Returns
    -------
    dict
        With keys:
            - ID
            - msg
            - type
            - desc"""
    sqlStr = """SELECT msg.id, msg.msg, msg.type, t.desc FROM messages msg
    JOIN types t ON msg.type = t.id"""
    with sql_connection() as con:
        cursor = con.cursor()
        cursor.execute(sqlStr)
        data = cursor.fetchall()
        return json.dumps(data)


def getMessageTableDataFrame() -> pd.DataFrame:
    """Get the messages table as a DataFrame

    Returns
    -------
    pd.DataFrame"""
    con = sql_connection()
    df = pd.read_sql("SELECT msg, type FROM messages", con)
    con.close()
    return df


def updateClassification(msgID: int, typeBool: bool):
    """This is to toggle an items classification

    Parameters
    ----------
    msgID: int
        The ID to update

    typeBool: bool
        The classification to change to"""
    con = sql_connection()
    cursor = con.cursor()
    cursor.execute("UPDATE messages SET type = ? WHERE id = ?",
                   (typeBool, msgID))
    con.commit()
    con.close()


def deleteMessage(msgID: int):
    """This is to delete a message from the messages table

    Parameters
    ----------
    msgID: int
        The message ID to delete"""
    con = sql_connection()
    cursor = con.cursor()
    cursor.execute("DELETE FROM messages WHERE id = ?", (msgID,))
    con.commit()
    con.close()
