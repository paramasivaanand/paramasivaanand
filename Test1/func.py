# def add(a,b):
#     c=a+b
#     return c
# # ad=add(10,20)
# # print(ad)
# def sub(a,b):
#     c=a-b
#     return c


import pymysql

conn = pymysql.connect(
        host='localhost',
        user='root',
        password ="",
        db='testdb',
        )
db=conn.cursor()
sql = "INSERT INTO persons (FirstName, Address) VALUES (%s, %s)"
val = ("John", "Highway 21")
db.execute(sql, val)
conn.commit()
db.execute("SELECT * FROM `persons` WHERE 1;")
t=db.fetchall()

print(t)
db.close()