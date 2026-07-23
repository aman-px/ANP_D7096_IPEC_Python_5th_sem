import mysql.connector

dataconnection = mysql.connector.connect(host = 'localhost',
    user = 'root',
    password = 'Sanji@007',
    database = 'StudentManagement')

cursorobj = dataconnection.cursor()

sql_query = 'select * from Student'

cursorobj.execute(sql_query)

data = False
for row in cursorobj:
    data = True
    print("Student Id : ",row[0])
    print("Student Name : ",row[1])
    print("Standard : ",row[2])
    print("Age : ",row[3],"Year")
    print("-------------------------------")

if data == False:
    print("No Data Found")

cursorobj.close()

dataconnection.close()