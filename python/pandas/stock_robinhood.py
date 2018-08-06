# script to get max stock value and current value of stock
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
  select_str = f"select date, {stock} from stock_price where {stock} = (select max({stock}) from stock_price);"
  try:
    cursor.execute(select_str)
  except:
    print ("ERROR", nsert_str)
  row = cursor.fetchall()
  print (stock, row)
db.commit()
db.close()
