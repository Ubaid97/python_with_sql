# Python with SQL
## Using PYODBC (open database connectivity) to connect to SQL from our Python program
- What is a Cursor and how to use it

**some functions that we can use to interact with SQL data**
- install pyodbc using ```pip install pyodbc```
- Set up pyobdc connection: ```import pyodbc```
- install odbc driver from: https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver15

- establish a connection:
```python
server = "databases1.spartaglobal.academy"
database = "Northwind"
username = "**"
password = "*******"
northwind_connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
```
- server name - database name - username and password is required to connect to pyodbc
verify connection:
```python
cursor = northwind_connection.cursor()
# cursor is location of your mouse/current path
cursor.execute("SELECT @@VERSION")
select the version of current DB
row = cursor.fetchone()
print(row)
```
- get data from a table in the DB:
```python
cust_row = cursor.execute("SELECT * FROM Customers;").fetchall()
```
- using fetchall() method we can get all the data in Customers table
- run queries:
```python
for records in cust_row:
    print(records)
```
