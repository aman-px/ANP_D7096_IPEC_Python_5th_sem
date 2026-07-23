import mysql.connector

dataconnection = mysql.connector.connect(host = 'localhost',
    user = 'root',
    password = 'Sanji@007',
    database = 'StudentManagement')

cursorobj = dataconnection.cursor()

sql_query ='''
delete from  Student
where stu_id = %s
'''
values = ("std101",)


cursorobj.execute(sql_query, values)
dataconnection.commit()

if(cursorobj.rowcount > 0):
    print("Data Deleted Successfully")
else:
    print("Unable to delete Data")

cursorobj.close()

dataconnection.close()