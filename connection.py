import pymysql
con=pymysql.connect(db='hcl',user='root',passwd='root',host='localhost')
cur=con.cursor()
for _ in range(3):
	id=(int)(input("enter dep number")) 
	city=input("enter dept  name")
	state=input("enter dept  name")
	lat_n=(int)(input("enter dep number"))
	long_w=(int)(input("enter dep number"))
	cur.execute("insert into station values(%d,'%s','%s',%d,%d)" %(id,city,state,lat_n,long_w))
	con.commit()
con.close()
print('record saved')