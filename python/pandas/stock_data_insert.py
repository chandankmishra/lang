#
# Script to import data from Robinhood and Yahoo and
# insert into a mysql database
#

import pandas_datareader.data as web
import datetime
import pandas as pd
import MySQLdb
import pdb
from yahoo_fin import stock_info as si

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

def insert_rows(cursor):
    select_query = f"select date from stock_price order by date desc limit 1;"
    try:
        cursor.execute(select_query)
    except:
        print ("ERROR", select_query)
    last_date = cursor.fetchall()
    start = last_date[0][0]
    end = datetime.date.today()
    while start < end:
        start += datetime.timedelta(days=1)
        insert_query = f"insert into stock_price values('{start}',0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0);"
        print (insert_query)
        try:
            cursor.execute(insert_query)
        except:
            print ("ERROR", insert_query)

def update_price_using_robinhood(cursor):
    # Fetch data from Robinhood
    end = datetime.date.today()
    start = end - datetime.timedelta(days=30)
    for stock in STOCKS:
      d = web.DataReader(stock, 'robinhood', start, end)
      #d = web.DataReader(stock, 'robinhood', '2018-08-06', '2018-08-06')
      dstr = str(d).split('\n')
      dstr = dstr[2:-2]
      for i in range(len(dstr)):
        tlst = dstr[i].split()
        if i == 0:
          company = tlst.pop(0)

        date_str = tlst[0]
        price = tlst[1]
        if date_str == '...':
          continue
        dd = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        update_query = "UPDATE stock_price SET {} = {} where date='{}';".format(company, price, dd)
        #print (update_query)
        try:
          cursor.execute(update_query)
        except:
          print ("ERROR", update_query)

def update_price_using_yahoo(cursor):
    # Fetch data from Yahoo
    for stock in STOCKS:
      try:
        d = web.DataReader(stock, 'yahoo', start, end)
        #d = web.DataReader(stock, 'yahoo', '2018-08-01', '2018-08-06')
      except:
        continue
      dstr = str(d).split('\n')
      dstr = dstr[2:-2]
      for row in dstr:
        price = row.split()[4]
        date_str = row.split()[0]
        try:
          if float(price) > 2000 or float(price) == 0.0:
            continue
        except:
          continue
        if date_str == '...':
          continue
        dd = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        update_query = "UPDATE stock_price SET {} = {} where date='{}';".format(stock, price, dd, stock)
        #print (update_query)
        try:
          cursor.execute(update_query)
        except:
          print ("ERROR", update_query)

def update_stock_analysis_table(cursor):
    # drop stock_price_analysis table
    query = f"drop table stock_price_analysis;"
    try:
        cursor.execute(query)
    except:
        print ("ERROR", query)

    # create stock_price_analysis table
    query = f"create table stock_price_analysis like stock_price;"
    try:
        cursor.execute(query)
    except:
        print ("ERROR", query)

    # copy stock_price table rows in to stock_price_analysis table
    query = f"insert stock_price_analysis select * from stock_price;;"
    try:
        cursor.execute(query)
    except:
        print ("ERROR", query)

    # get all rows from stock_price_analysis table
    query = f"select * from stock_price_analysis;"
    try:
        cursor.execute(query)
    except:
        print ("ERROR", query)
    #breakpoint()
    all_records = cursor.fetchall()
    priv_record = list(all_records[0])
    for record in all_records:
        date_str = record[0]
        if date_str == '...':
          continue
        dd = date_str
        for idx, stock in enumerate(STOCKS):
            idx = idx+1
            if record[idx] > 0.0:
                priv_record[idx] = record[idx]
                continue
            price = priv_record[idx]
            update_query = "UPDATE stock_price_analysis SET {} = {} where date='{}';".format(stock, price, dd, stock)
            #print (update_query)
            try:
              cursor.execute(update_query)
            except:
              print ("ERROR", update_query)

    # update todays price
    today = datetime.date.today()
    price = 0.0
    for idx, stock in enumerate(STOCKS):
        try:
            price = si.get_live_price(stock)
        except:
            pass
        update_query = "UPDATE stock_price_analysis SET {} = {} where date='{}';".format(stock, price, today)
        try:
          cursor.execute(update_query)
        except:
          print ("ERROR", update_query)

def main():
    """
    main driver program
    """
	cursor = connect_mysql_db()
	print("Insert new rows in stock price table..")
	insert_rows(cursor)
	print("Update stock price table..")
	update_price_using_robinhood(cursor)
	update_price_using_yahoo(cursor)
	print("Update stock price analysis table..")
	update_stock_analysis_table(cursor)
	close_mysql_db()

if __name__ == "__main__":
    main()

#end of file
