import mysql.connector

dataconnection = mysql.connector.connect(host = 'localhost',
    user = 'root',
    password = 'Sanji@007',
    database = 'StudentManagement')

cursorobj = dataconnection.cursor()

sql_query = 'insert into Student values(%s,%s,%s,%s)'

Student = [('101','Aman','12th',20),('102','Ankit','B.tech',22),('103','Sudarshan','MCA',27),('104','Gulshan','Inter',18),('105','Sneha','BCA',24)]


cursorobj.executemany(sql_query,Student)
dataconnection.commit()

if(cursorobj.rowcount > 0):
    print("Data Inserted Successfully")
else:
    print("Unable to Insert Data")

cursorobj.close()

dataconnection.close()