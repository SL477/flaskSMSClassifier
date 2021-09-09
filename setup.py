# This is to run the first time setup
import dbHelper as dbHelper
import pandas as pd
from os import path

# Get the data from the TSV files
def getTSVDataFrame(fileName):
    """
    This gets the dataframe from the file name
    """
    df_ret = pd.read_csv(fileName, header=None, sep='\t', names=['type','msg'])
    df_ret['type'] = df_ret['type'] == 'ham'
    return df_ret

if __name__ == '__main__':
    dbHelper.firstTimeSetup()
    df = getTSVDataFrame(path.join('data', 'train-data.tsv'))
    con = dbHelper.sql_connection()
    #print(df.head())
    for index, row in df.iterrows():
        #print(row['msg'],row['type'])
        dbHelper.insertDataIntoMessages(con, row['msg'], row['type'])
    con.close()