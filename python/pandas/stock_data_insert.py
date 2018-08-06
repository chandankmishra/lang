# Script to import data from Robinhood and Yahoo and insert into a database

import pandas_datareader.data as web
import datetime
import pandas as pd
import MySQLdb
import pdb

end = datetime.date.today()
start = end - datetime.timedelta(days=100)
stocks = ['TWTR', 'NFLX', 'FB', 'TSLA', 'DBX', 'AMZN', 'GOOG', 'ZS', 'AMD', 'SNAP', 'MSFT', 'ADBE', 'BABA', 'PANW', 'ORCL', 'NVDA', 'VMW', 'ANET', 'YELP', 'INTU']
res = {}
result = []

db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="root",
                     db="tmp")
cursor = db.cursor()

# Fetch data from Robinhood
for stock in stocks:
  d = web.DataReader(stock, 'robinhood', '2015-02-01', '2015-03-01')
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
    insert_str = "UPDATE stock_price SET {} = {} where date='{}';".format(company, price, dd)
    print (insert_str)
    try:
      cursor.execute(insert_str)
    except:
      print ("ERROR", nsert_str)

  # Fetch data from Yahoo
  for stock in stocks:
    try:
      d = web.DataReader(stock, 'yahoo', '2016-05-01', '2016-05-31')
    except:
      continue
    dstr = str(d).split('\n')
    dstr = dstr[2:-2]
    company = stock
    for i in range(len(dstr)):
      tlst = dstr[i].split()
      date_str = tlst[0]
      price = tlst[5]
      try:
        if float(price) > 2000 or float(price) == 0.0:
          continue
      except:
        continue
      if date_str == '...':
        continue
      dd = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
      insert_str = "UPDATE stock_price SET {} = {} where date='{}';".format(company, price, dd, company)
      print (insert_str)
      try:
        cursor.execute(insert_str)
      except:
        print ("ERROR", nsert_str)

db.commit()
db.close()
