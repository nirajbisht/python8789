import pymysql
con=pymysql.connect(db='hcl',user='root',passwd='root',host='localhost')
cur=con.cursor()
depno=(int)(input("enter dep number"))
cur.execute("update dept set depname='neeraj'where depno=%d" %(depno))
result = cur.fetchall()
con.commit()
if (result):
	print(result)
	
	
	
	