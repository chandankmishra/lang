import pandas_datareader.data as web
import datetime
import pandas as pd
import MySQLdb
import pdb

#start = datetime.datetime(2018,7,25)
end = datetime.date.today()
delta = datetime.timedelta(days=30)
start = end-delta
apple = web.DataReader("AAPL", "yahoo", start, end)
#print (apple.head())

stocks = ['ORCL', 'TSLA', 'IBM','YELP', 'MSFT']
d = {}
for stock in stocks:
    d[stock] = web.DataReader(stock, 'yahoo',start,end)
pan = pd.Panel(d)
#pdb.set_trace()
df = pan.minor_xs('Close')
print (df)
for index, row in df.iterrows():
    print (str(index).split()[0], row['ORCL'], row['TSLA'])


'''
db = MySQLdb.connect(host= "localhost",
                  user="root",
                  passwd="root",
                  db="tmp")
cursor = db.cursor()
cursor.execute("SELECT * FROM tmp_table;")
#cursor.execute("INSERT INTO tmp_table VALUES ('%s','%s','%s') ", (1,'APPL', 200.200))
row = cursor.fetchall()
print (row)
print (apple.loc['2018-02-09'])
for row in apple:
    for col in apple[row]:
        print (col, end=' ')
    print ('')
'''
