import mysql.connector

dataconnection = mysql.connector.connect(host = 'localhost',
    user = 'root',
    password = 'Sanji@007',
    database = 'StudentManagement')

cursorobj = dataconnection.cursor()

sql_query ='''
update  Student
set  stu_name = %s,standard = %s,age=%s 
where stu_id = %s
'''
values = ("Lucky","B.Tech",18,"105")


cursorobj.execute(sql_query,values)
dataconnection.commit()

if(cursorobj.rowcount > 0):
    print("Data Updated Successfully")
else:
    print("Unable to update Data")

cursorobj.close()

dataconnection.close()