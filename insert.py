import pymysql
con=pymysql.connect(db='hcl',user='root',passwd='root',host='localhost')
cur=con.cursor()
n=(int)(input("enter dep number"))
salary=(int)(input("enter salary"))
cur.execute("select * from dept where depno=%d "%(n))
result = cur.fetchall
if (ressult);
	print("duplicate record")
else:
	cur.execute(insert into dept vaules(343,'harshit',2354)
	con.commit()
	