import time 
import datetime
import requests
import pandas as pd
import pandas_datareader.data as web
import datetime
import pandas as pd
import MySQLdb
import pdb
import argparse

print (datetime.date.today())
DB = None
def connect_mysql_db():
    global DB
    DB = MySQLdb.connect(host="localhost",
                         user="root",
                         passwd="root",
                         db="tmp")
    return DB.cursor()


def close_mysql_db():
    DB.commit()
    DB.close()

def update_column(cursor, column, val, key): 
    select_str = f"select count(*) from INFORMATION_SCHEMA.COLUMNS where table_name='daily_stock' and column_name='{column}';"
    result = cursor.execute(select_str)
    result=cursor.fetchone()
    if int(result[0]) > 0:
        insert_query = "UPDATE daily_stock SET {} = {} where tstamp='{}';".format(column, val, key)
        print (insert_query)
        try:
            cursor.execute(insert_query)
        except:
            print ("ERROR", insert_query)
        return

    delete_query = f"alter table daily_stock add {column} float default {val};"
    print (delete_query)
    try:
        cursor.execute(delete_query)
    except:
        print ("ERROR", delete_query)

def mark_valid(cursor, key): 
    insert_query = "UPDATE daily_stock SET valid = {} where tstamp='{}';".format(1, key)
    print (datetime.datetime.now())
    print (insert_query)
    try:
        cursor.execute(insert_query)
    except:
        print ("ERROR", insert_query)
    print (datetime.datetime.now())

    query = "select tstamp, valid from daily_stock where valid={};".format(1)
    try:
        cursor.execute(query)
    except:
        print ("ERROR", query)
    all_records = cursor.fetchall()
    print (all_records)

    query = "select max(tstamp) from daily_stock where valid={};".format(1)
    try:
        cursor.execute(query)
    except:
        print ("ERROR", query)
    all_records = cursor.fetchall()
    print ("max:", all_records)

    query = "select min(tstamp) from daily_stock where valid={};".format(1)
    try:
        cursor.execute(query)
    except:
        print ("ERROR", query)
    all_records = cursor.fetchall()
    print ("min:", all_records)

def update_rows(cursor, key):
    url = 'https://www.tradingview.com/markets/stocks-usa/market-movers-gainers/'
    html = requests.get(url).content
    df_list = pd.read_html(html)
    df = df_list[-1]
    n = len(df)
    for i in range(n):
        company = df.iloc[i][0].split()[0]
        price = float(df.iloc[i][1])
        update_column(cursor, company, price, key)
    mark_valid(cursor, key)

def insert_rows(cursor): 
    # drop table
    delete_query = f"drop table daily_stock;"
    print (delete_query)
    try:
        cursor.execute(delete_query)
    except:
        print ("ERROR", delete_query)

    # create table
    delete_query = f"create table daily_stock (tstamp varchar(255), valid int);"
    print (delete_query)
    try:
        cursor.execute(delete_query)
    except:
        print ("ERROR", delete_query)

    # insert empty rows
    now = datetime.datetime.now()
    print (datetime.datetime.now())
    minute=now.minute
    hour=now.hour
    for m in range(800):
        minute = (now.hour * 60 + now.minute + m) % 60
        hour = (now.hour * 60 + now.minute + m) // 60
        key = f"{now.year}:{now.month}:{now.day}:{hour}:{minute}"
        insert_query = f"insert into daily_stock values('{key}', 0);"
        print (insert_query)
        try:
            cursor.execute(insert_query)
        except:
            print ("ERROR", insert_query)

def copy_daily_table(cursor):
    # drop daily_stock_analysis table
    query = f"drop table daily_stock_analysis;"
    try:
        cursor.execute(query)
    except:
        print ("ERROR", query)

    # create daily_stock_analysis table
    query = f"create table daily_stock_analysis like daily_stock;"
    try:
        cursor.execute(query)
    except:
        print ("ERROR", query)

    # copy daily_stock table rows in to daily_stock_analysis table
    query = f"insert daily_stock_analysis select * from daily_stock;"
    try:
        cursor.execute(query)
    except:
        print ("ERROR", query)

    # get all rows from daily_stock table
    query = f"select * from daily_stock;"
    try:
        cursor.execute(query)
    except:
        print ("ERROR", query)
    all_records = cursor.fetchall()
    print (all_records)

def stock_analysis(DAYS):
    """
    stock_analysis driver program
    """
    results = []
    cursor = connect_mysql_db()
    insert_rows(cursor)
    close_mysql_db()
    try:
        while True:
            now = datetime.datetime.now()
            key = f"{now.year}:{now.month}:{now.day}:{now.hour}:{now.minute}"
            print("time:", now, " key:", key)
            cursor = connect_mysql_db()
            update_rows(cursor, key)
            time.sleep(15)
            close_mysql_db()
            time.sleep(15)
    except:
        pass

if __name__ == "__main__":
# initiate the parser
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument("--days", "-d", help="set number of days")
    ARGS = PARSER.parse_args()
    if ARGS.days is None:
        DAYS = 30
    else:
        DAYS = int(ARGS.days)
    print("Show stock analysis sorted by:", DAYS)
    stock_analysis(DAYS)

#end of file
