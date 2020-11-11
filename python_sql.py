# This lesson will include connection to our SQL DB from Python using PYODBC

# pyodbc driver from microsoft helps us to connect to SQL instance
# we will connect to our Northwind DB which you have already used in SQL week

import pyodbc

server = "databases1.spartaglobal.academy"
database = "Northwind"
username = "**"
password = "*******"
northwind_connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
# server name - database name - username and password is required to connect to pyodbc
cursor = northwind_connection.cursor()
# cursor is location of your mouse/current path
cursor.execute("SELECT @@VERSION")
# select the version of current DB
row = cursor.fetchone()
print(row)

# In our DB, we have a table Customers with customers' data
# cust_row = cursor.execute("SELECT * FROM Customers;").fetchall()
# using fetchall() method we can get all the data in Customers table
# print(cust_row)
# for records in cust_row:
#     print(records)

# Products table
# product_rows = cursor.execute("SELECT * FROM Products").fetchall()
# for pr_records in product_rows:
#     print(pr_records.UnitPrice)

# product_row = cursor.execute("SELECT * FROM Products")
# loop ensures we only iterate through data as long as data is available
# while True:
#     records = product_row.fetchone()
#     if records is None:
#         break
#     print(records.UnitPrice)
