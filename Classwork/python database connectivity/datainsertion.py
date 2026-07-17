#to import mysql.connector module
import mysql.connector
#------------------------------------------------------------
#to establish connection with mysql
dataconnection = mysql.connector.connect(host = 'localhost',
	user = 'root',
	password = 'Obito@007',
	database = 'Studentmanagement'
	)
#------------------------------------------------------------
# to create a cursor object
cursorobj = dataconnection.cursor()
#------------------------------------------------------------
# writing insert query
sql_query = 'insert into Student values (%s,%s,%s,%s)'

#------------------------------------------------------------
std_id ='std101'
std_name = 'Anil'
standard = '10th'
age = 15
#put the values to be inserted inside a tuple
values = (std_id,std_name,standard,age)
#------------------------------------------------------------
#to execute the query
cursorobj.execute(sql_query , values)
#------------------------------------------------------------
#to commit changes
dataconnection.commit()
#------------------------------------------------------------
#to check data inserted or not
if(cursorobj.rowcount  > 0):
	print("Data inserted successfully")
else:
	print("Unable to insert data")

print(cursorobj.rowcount, "Record Inserted") 
#------------------------------------------------------------
#to close cursur object
cursorobj.close()
#to close connection object
dataconnection.close()
#------------------------------------------------------------
