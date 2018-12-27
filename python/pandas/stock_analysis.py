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

def get_max_stock_price_analysis(results, cursor):
    """
    Get the max stock price in the current year
    @todo: remove hardcoding for 2018.
    """
    for stock in STOCKS:
      select_str = f"select date, {stock} from stock_price_analysis where {stock} = (select max({stock}) from stock_price_analysis where date >= '2018-01-01 00:00:00');"
      try:
        cursor.execute(select_str)
      except:
        print ("ERROR", nsert_str)
      row = cursor.fetchall()
      date, price = row[0][0], row[0][1]
      results.append([stock, str(date), price])

def get_max_stock_price_analysis_days(results, cursor, date):
    """
    Get the max stock price in the current year
    @todo: remove hardcoding for 2018.
    """
    for stock in STOCKS:
      select_str = f"select date, {stock} from stock_price_analysis where {stock} = (select max({stock}) from stock_price_analysis where date >= {date});"
      try:
        cursor.execute(select_str)
      except:
        print ("ERROR", nsert_str)
      row = cursor.fetchall()
      date, price = row[0][0], row[0][1]
      results.append([stock, str(date), price])

def get_last_date(cursor):
    """
    Get the last entry with valid data
    """
    select_str = f"select *  from stock_price_analysis order by date desc limit 10;"
    try:
        cursor.execute(select_str)
    except:
        print ("ERROR", nsert_str)
    current_price = cursor.fetchall()
    for row in range(len(current_price)):
        cur_row = current_price[row]
        if cur_row[1] > 0.0:
            return datetime.datetime.strptime(str(cur_row[0]), "%Y-%m-%d").date()
    return datetime.date.today()

def get_current_price(results, cursor):
    """
    Get the current date stock price
    @todo: find the last entry with valid data
    """
    last_date = get_last_date(cursor)
    select_str = "select * from stock_price_analysis where date = '{}';".format(last_date)
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
    select_str = f"select * from stock_price_analysis where date = '2018-01-01 00:00:00';"
    try:
        cursor.execute(select_str)
    except:
        print ("ERROR", nsert_str)
    start_price = cursor.fetchall()
    for i, price in enumerate(start_price[0][1:]):
        if i == len(results): break
        results[i].append(price)

def update_todays_price(results, cursor):
    """
    Get the price at year start
    @todo: find the first valid date in the year
    """
    today = datetime.date.today()
    for idx, stock in enumerate(STOCKS):
      # get the today's price
      select_str = f"select {stock} from stock_price_analysis where date = '{today} 00:00:00';"
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
      select_str = f"select {stock} from stock_price_analysis where date = '{before} 00:00:00';"
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
      select_str = f"select {stock} from stock_price_analysis where {stock} = (select max({stock}) from stock_price_analysis where date >= '{before} 00:00:00');"
      try:
        cursor.execute(select_str)
      except:
          raise
      row = cursor.fetchall()
      price = row[0][0]
      results[idx].append(price)

      # get the min price
      select_str = f"select {stock} from stock_price_analysis where {stock} = (select min({stock}) from stock_price_analysis where date >= '{before} 00:00:00');"
      try:
        cursor.execute(select_str)
      except:
          raise
      row = cursor.fetchall()
      price = row[0][0]
      results[idx].append(price)

def get_prev_stock_price(results, cursor):
    """
    Get the price at year start
    @todo: find the first valid date in the year
    """
    update_todays_price(results, cursor)
    update_old_stock_price(results, cursor, 1)
    update_old_stock_price(results, cursor, 7)
    update_old_stock_price(results, cursor, 30)
    update_old_stock_price(results, cursor, 90)
    update_old_stock_price(results, cursor, 365)

def display_result(results):
    """
    Display the result of analysis in tabular format
    """
    # r[15] is % change in 30days
    results = sorted(results, key=lambda x:-float(x[7][:-1]))
    print ('% increase\tcompany\t\tcurrent\t\thighest\t1d%\t\t7d%\t\t30d%\t\t90d%\t\t365d%')
    for r in results:
        print ('{0}%\t\t{1}\t\t{2}\t\t{3}\t{4}\t\t{5}\t\t{6}\t\t{7}\t\t{8}'.format(r[0], r[1], r[6], r[3], r[7], r[11], r[15], r[19], r[23]))

def main():
    """
    main driver program
    """
    results = []
    cursor = connect_mysql_db()
    get_max_stock_price_analysis(results, cursor)
    get_current_price(results, cursor)
    get_year_start_price(results, cursor)
    get_prev_stock_price(results, cursor)
    display_result(results)
    '''
    for result in results:
        print (result)
    '''
    close_mysql_db()

if __name__ == "__main__":
    main()

#end of file
