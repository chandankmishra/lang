import pandas_datareader.data as web
import datetime
import pandas as pd
import MySQLdb
import pdb

end = datetime.date.today()
start = end - datetime.timedelta(days=100)
# stocks = ['TWTR']
stocks = ['TWTR', 'NFLX', 'FB', 'TSLA', 'DBX', 'AMZN', 'GOOG', 'ZS', 'AMD', 'SNAP', 'MSFT', 'ADBE', 'BABA', 'PANW', 'ORCL', 'NVDA', 'VMW', 'ANET', 'YELP', 'INTU']
res = {}
result = []

db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="root",
                     db="tmp")
cursor = db.cursor()

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
# insert_str = "UPDATE stock_price SET TWTR = 0.0 where TWTR='16.07';"
# cursor.execute(insert_str)
db.commit()
db.close()

# select * from stock_price where TWTR BETWEEN 16.06 and 16.08 and NFLX <1;
# select * from stock_price where TWTR BETWEEN 16.06 and 16.08 and DATE(date) <  DATE('2013-11-06');
# update stock_price SET TWTR = 0.0 where TWTR BETWEEN 16.06 and 16.08 and DATE(date) <  DATE('2013-11-06');
