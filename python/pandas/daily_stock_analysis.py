#
# script to get max stock value and current value of stock
#

import pandas_datareader.data as web
import datetime
import pandas as pd
import MySQLdb
import pdb
import argparse

STOCKS = ['TWTR', 'NFLX', 'FB', 'TSLA', 'DBX', 'AMZN', 'GOOG', 'ZS', 'AMD', 'AAPL', 'SNAP', 'MSFT', 'ADBE', 'BABA', 'PANW', 'ORCL', 'NVDA', 'VMW', 'ANET', 'YELP', 'INTU', 'ROKU', 'SQ','TWLO']

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

def get_last_date(cursor):
    """
    Get the last entry with valid data
    """
    select_str = f"select *  from daily_stock_analysis order by date desc limit 10;"
    try:
        cursor.execute(select_str)
    except:
        print("ERROR", nsert_str)
    current_price = cursor.fetchall()
    for row in range(len(current_price)):
        cur_row = current_price[row]
        if cur_row[1] > 0.0:
            return datetime.datetime.strptime(str(cur_row[0]), "%Y-%m-%d").date()
    return datetime.date.today()

def update_todays_price(results, cursor):
    """
    Get the price at year start
    @todo: find the first valid date in the year
    """
    today = datetime.date.today()
    for idx, stock in enumerate(STOCKS):
      # get the today's price
      select_str = f"select {stock} from daily_stock_analysis where date = '{today} 00:00:00';"
      try:
        cursor.execute(select_str)
      except:
          raise
      row = cursor.fetchall()
      price = row[0][0]
      results[idx].append(price)

def get_percent_change(start, end):
    """
    Get the current date stock price
    @todo: find the last entry with valid data
    """
    increase = 0.0
    if start > 0.0:
        increase = "{0}%".format(round(((end -  start) * 100) / start, 2))
    return increase


def update_old_stock_price(results, cursor, days):
    """
    Get the price at year start
    @todo: find the first valid date in the year
    """
    today = datetime.date.today()
    before = today - datetime.timedelta(days=days)
    for idx, stock in enumerate(STOCKS):
      # get the price before N days
      select_str = f"select {stock} from daily_stock_analysis where date = '{before} 00:00:00';"
      try:
        cursor.execute(select_str)
      except:
          raise
      row = cursor.fetchall()
      price = row[0][0]
      today_price = results[idx][6]
      results[idx].append(get_percent_change(price, today_price))
      results[idx].append(price)

      # get the max price
      select_str = f"select {stock} from daily_stock_analysis where {stock} = (select max({stock}) from daily_stock_analysis where date >= '{before} 00:00:00');"
      try:
        cursor.execute(select_str)
      except:
          raise
      row = cursor.fetchall()
      price = row[0][0]
      results[idx].append(price)

      # get the min price
      select_str = f"select {stock} from daily_stock_analysis where {stock} = (select min({stock}) from daily_stock_analysis where date >= '{before} 00:00:00');"
      try:
        cursor.execute(select_str)
      except:
          raise
      row = cursor.fetchall()
      price = row[0][0]
      results[idx].append(price)

def get_time_min_max(cursor, cols):
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
    max_record = cursor.fetchall()
    print ("max:", max_record[0][0])

    query = "select min(tstamp) from daily_stock where valid={};".format(1)
    try:
        cursor.execute(query)
    except:
        print ("ERROR", query)
    min_record = cursor.fetchall()
    print ("min:", min_record[0][0])

    query = "select * from INFORMATION_SCHEMA.COLUMNS where table_name='daily_stock';"
    try:
        cursor.execute(query)
    except:
        print ("ERROR", query)
    result = cursor.fetchall()

    n = len(result)
    for i in range(2,n):
        cols.append(result[i][3])
        
    return min_record[0][0], max_record[0][0] 

def get_stock_data(cursor, cols, start_time, end_time, result):
    for stock in cols:
        query = "select {} from daily_stock where tstamp='{}';".format(stock, start_time)
        try:
            cursor.execute(query)
        except:
            print ("ERROR", query)
        start_record = cursor.fetchall()

        query = "select {} from daily_stock where tstamp='{}';".format(stock, end_time)
        try:
            cursor.execute(query)
        except:
            print ("ERROR", query)
        end_record = cursor.fetchall()
        
        change = (end_record[0][0] - start_record[0][0]) / start_record[0][0] 

        query = "select min({}) from daily_stock;".format(stock)
        try:
            cursor.execute(query)
        except:
            print ("ERROR", query)
        min_record = cursor.fetchall()
    
        query = "select max({}) from daily_stock;".format(stock)
        try:
            cursor.execute(query)
        except:
            print ("ERROR", query)
        max_record = cursor.fetchall()
        result.append((change, stock, start_record[0][0], end_record[0][0], min_record[0][0], max_record[0][0]))

def stock_analysis(DAYS):
    """
    stock_analysis driver program
    """
    results = []
    cursor = connect_mysql_db()
    now = datetime.datetime.now()
    key = f"{now.year}:{now.month}:{now.day}:{now.hour}:{now.minute}"
    cols = []
    start_time, end_time = get_time_min_max(cursor, cols)
    get_stock_data(cursor, cols, start_time, end_time, results)
    results.sort()
    print ("STOCK\tCHANGE\t\tSTART\t\tEND\t\tMIN\t\tMAX")
    for result in results:
        print (round(result[0],2), "\t", result[1], "\t\t", result[2], "\t\t", result[3], "\t\t", round(result[4],2), "\t\t", round(result[5],2)) 
    close_mysql_db()

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
