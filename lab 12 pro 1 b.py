import cxOracle
con=cxOracle.connect('system/cdac1234@localhost:1521/orcl')
data=("select name from client_master")
cursor=con.cursor()
cursor.execute(data)
con.commit()
x=cursor.fetchall()
for i in x:
 if i[0][1]=="A":
     print(i[0])
print("successfully run")
cursor.close()
con.close()
