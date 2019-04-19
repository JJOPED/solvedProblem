"""
将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。(mySQL Server)
"""

#把数据插入到一个数据库的表格中
#Python与mySQL Server交互（部分）

import pymssql
"""
try:
    Info = {
        'host': '127.0.0.1:1433',
        'user': 'sa',
        'password': '123',
        'database': 'mySQL_test',
        'charset': 'utf8'
    }
    connect = pymssql.connect(host='127.0.0.1:1433', user='sa', password='123', database='mySQL_test', charset='utf8')
    #connect = pymssql.connect(Info)#好像不可以
    print("successful!")
except Exception as e:
    print(e)
    print("连接数据库失败")

cur = connect.cursor()
sql1 = 'select * from student'
cur.execute(sql1)#tuple:元组
#print(type(cur))#pymssql.Cursor
#print(type(cur.fetchone()))
for row in cur:#不是cur.fetchall()
    #print(type(row))#row是tuple类型
    print(row[0])
"""

try:
    connect = pymssql.connect(host='127.0.0.1:1433', user='sa', password='123', database='mySQL_test', charset='utf8')
except Exception as e:
    print(e)
cur = connect.cursor()
sql_create = "create table Activation_code(id int, code char(9))"
sql_drop = "drop table Activation_code"

with cur:
    try:
        cur.execute(sql_drop)
    except Exception as e:
            print(e)
    try:
        cur.execute(sql_create)
    except Exception as e:
            print(e)
    i = 1
    with open("F:\wallPaper\\forTest\\ans.txt", "r") as f:
        #f.seek(0)
        for line in f:#line自动读取
            #str = f.readline()#这个时候，f会读取一行数据，然后for循环有会读取一段数据，导致最后5行数据只有偶数行能读到str并输出
            str = line.replace('\n', '')
            print(str)

            # sql_insert = 'insert into ansYZM(id,yzm) values('+(i, str) +')'
            # cur.execute(sql_insert)

            cur.execute('insert into Activation_code(id, code) values(%s,%s)', (i, str))
            i = i+1
    cur.execute('select * from Activation_code')
    print(cur.fetchall())
    cur.close()