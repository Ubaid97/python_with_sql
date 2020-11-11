# Pyodbc Task
**Task:**
- Create a new file and a class with function to establish connection with pyodbc
- create a function that create a table in the DB
- create a function that prompts user to input data in that table
- create a new file called PYODBC_TASK.md and document the steps to implement the task
 
## steps
- Create a new file and ```import pyodbc``` to establish pyodbc connection
- create new class, and inside the ```__init__``` function establish a connection to northwind database:
```python
def __init__(self):
    # the following block of code is used to establish a pyodbc connection to northwind database
    self.server = "databases1.spartaglobal.academy"
    self.database = "Northwind"
    self.username = "SA"
    self.password = "Passw0rd2018"
    self.northwind_connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password)
    # server name - database name - username and password is required to connect to pyodbc
    self.cursor = self.northwind_connection.cursor()
```
- define:
   - an emtpy string to store the table name:
```python
self.table_name = ""
```
   -  an empty list to store the column names of the user's table
```python
self.column_name = []
```
   - and an empty list which will store the datatypes of the table's columns
   ```python
self.column_datatype = []
```
**Create a function to create a table**
- allow the user to input the name of the table, and store it in the table_name variable:
```python
self.table_name = input("Enter the table name: ")
```
- use a while loop to allow user to add multiple columns to their table:
```python
while i < 3:
    # user asked to input the name of the table's first column
    self.column_name.append(input(f"Please enter the name of column {i}: ")) # name is added to column_name list (see line 16)
    # user asked to input the datatype of the table's first column
    self.column_datatype.append(input(f"Please enter the datatype of column {i}: ").upper())
    # datatype is added to column_datatype list (see line 17)
    i += 1 # counter is incremented by 1 in each iteration of while loop
```
- use following line of code to execute sql command for creating new table:
```python
table = self.cursor.execute(
            f"CREATE TABLE {self.table_name} ( {self.column_name[0]} {self.column_datatype[0]}, {self.column_name[1]} {self.column_datatype[1]} )")
```
**Create a function that prompts user to input data in th table**
- given that the table has two columns, ask user if they'd like to input data into the first column:
```python
column_2 = input(f"Would you like to input data for {self.column_name[1]}? Y/N ").upper()
```
- if they respond yes, ask them for the data they'd like to input and store it in a variable:
```python
if column_1 == "Y":
    column_1_data = input("Please enter the data you'd like to add: ")
```
- do the same for the second column:
```python
if column_2 == "Y":# if yes...
    column_2_data = input("Please enter the data you'd like to add: ")
```
- use the following line of code to insert the values entered by the user into their table:
```python
table_data = self.cursor.execute(f"INSERT INTO {self.table_name} ({self.column_name[0]}, {self.column_name[1]}) VALUES ('{column_1_data}', '{column_2_data}')")
```
**Create a function display the table's data**
- use the following line of code to get all the data in the table:
```python
table_rows = self.cursor.execute(f"SELECT * FROM {self.table_name}").fetchall() # using fetchall() method we can get all the data in the table
``` 
- use a for loop to print out the rows in the table:
```python
for records in table_rows:
    print(records)
```
**Execute the functions**
- create an instance of the class:
```python
test_run = PyodbcTask()
```
- and call each function using the instance:
```python
test_run.create_table() # running function to create a table
test_run.input_data() # running function to input data into created table
test_run.display_table() # running function to display data in the table
```