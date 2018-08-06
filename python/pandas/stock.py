import pandas_datareader.data as web
import datetime
import pandas as pd
import MySQLdb
import pdb

end = datetime.date.today()
start = end - datetime.timedelta(days=100)
stocks = ['TWTR']
# stocks = ['TWTR', 'NFLX', 'FB', 'TSLA', 'DBX', 'AMZN', 'GOOG', 'ZS', 'AMD', 'SNAP', 'MSFT', 'ADBE', 'BABA', 'PANW', 'ORCL', 'NVDA', 'VMW', 'ANET', 'YELP', 'INTU']
res = {}
result = []

db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="root",
                     db="tmp")
cursor = db.cursor()

for stock in stocks:
  d = web.DataReader(stock, 'robinhood', '2018-01-01', '2018-02-01')
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
db.commit()
db.close()
