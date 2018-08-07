#
# script to get max stock value and current value of stock
#

import pandas_datareader.data as web
import datetime
import pandas as pd
import MySQLdb
import pdb

STOCKS = ['TWTR', 'NFLX', 'FB', 'TSLA', 'DBX', 'AMZN', 'GOOG', 'ZS', 'AMD', 'AAPL', 'SNAP', 'MSFT', 'ADBE', 'BABA', 'PANW', 'ORCL', 'NVDA', 'VMW', 'ANET', 'YELP', 'INTU']

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

def get_max_stock_price(results, cursor):
    """
    Get the max stock price in the current year
    @todo: remove hardcoding for 2018.
    """
    for stock in STOCKS:
      select_str = f"select date, {stock} from stock_price where {stock} = (select max({stock}) from stock_price where date >= '2018-01-01 00:00:00');"
      try:
        cursor.execute(select_str)
      except:
        print ("ERROR", nsert_str)
      row = cursor.fetchall()
      date, price = row[0][0], row[0][1]
      results.append([stock, str(date), price])

def get_current_price(results, cursor):
    """
    Get the current date stock price
    @todo: find the last entry with valid data
    """
    select_str = f"select *  from stock_price order by date desc limit 1;"
    try:
        cursor.execute(select_str)
    except:
        print ("ERROR", nsert_str)
    current_price = cursor.fetchall()
    for i, price in enumerate(current_price[0][1:]):
        if i == len(results): break
        results[i].append(price)
        increase = 0.0
        if price > 0.0:
            increase = "{0}".format(round(((results[i][2] - price) * 100) / price, 2))
        results[i].insert(0, float(increase))

def get_year_start_price(results, cursor):
    """
    Get the price at year start
    @todo: find the first valid date in the year
    """
    select_str = f"select * from stock_price where date = '2018-01-02 00:00:00';"
    try:
        cursor.execute(select_str)
    except:
        print ("ERROR", nsert_str)
    start_price = cursor.fetchall()
    for i, price in enumerate(start_price[0][1:]):
        if i == len(results): break
        results[i].append(price)

def display_result(results):
    """
    Display the result of analysis in tabular format
    """
    results = sorted(results, key=lambda x:-x[0])
    print ('% increase\tcompany\tdate\t\tyear-start\tcurrent\thighest')
    for r in results:
        print ('{0}%\t\t{1}\t{2}\t{3}\t\t{4}\t{5}'.format(r[0], r[1], r[2], r[5], r[4], r[3]))

def main():
    """
    main driver program
    """
    results = []
    cursor = connect_mysql_db()
    get_max_stock_price(results, cursor)
    get_current_price(results, cursor)
    get_year_start_price(results, cursor)
    display_result(results)
    close_mysql_db()

if __name__ == "__main__":
    main()

#end of file
