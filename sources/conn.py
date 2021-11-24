import pymysql

from tajne import login,haslo,baza

conn = pymysql.connect(host='localhost',port=3306, user=login, passwd=haslo, db=baza,charset="utf8")
cur = conn.cursor()

cur.execute("SELECT * FROM T1")
for response in cur:
    print(response[0])
    

cur.close()
#conn.commit()
conn.close() 
