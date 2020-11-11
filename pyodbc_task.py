import pyodbc # to setup pyodbc connection

class PyodbcTask:

    def __init__(self):
        # the following block of code is used to establish a pyodbc connection to northwind database
        self.server = "databases1.spartaglobal.academy"
        self.database = "Northwind"
        self.username = "SA"
        self.password = "Passw0rd2018"
        self.northwind_connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password)
        # server name - database name - username and password is required to connect to pyodbc
        self.cursor = self.northwind_connection.cursor()
        # defining variables to be used later in functions
        self.table_name = "" # an empty string to store the name of the table user will want to create
        self.column_name = [] # list which will store the column names of the user's table
        self.column_datatype = [] # list which will store the datatypes of the table's columns

    # function that creates a table
    def create_table(self):
        # user is asked to input the name they want to give the table
        self.table_name = input("Enter the table name: ") # name stored in table_name variable (see line 15)
        i = 1 # will be used as a counter for the while loop
        # while loop with 2 iterations, allowing the user to create a table with two columns
        while i < 3:
            # user asked to input the name of the table's first column
            self.column_name.append(input(f"Please enter the name of column {i}: ")) # name is added to column_name list (see line 16)
            # user asked to input the datatype of the table's first column
            self.column_datatype.append(input(f"Please enter the datatype of column {i}: ").upper())
            # datatype is added to column_datatype list (see line 17)
            i += 1 # counter is incremented by 1 in each iteration of while loop

        # used to execute sql commands
        table = self.cursor.execute(
            f"CREATE TABLE {self.table_name} ( {self.column_name[0]} {self.column_datatype[0]}, {self.column_name[1]} {self.column_datatype[1]} )")
        # sql command for creating a table with the table name, column names, and column datatypes entered by the user
        return table

    # function to input data into a table
    def input_data(self):
        # user is asked if they want to input data for the table's first column
        column_1 = input(f"Would you like to input data for {self.column_name[0]}? Y/N ").upper()
        if column_1 == "Y": # if yes...
            column_1_data = input("Please enter the data you'd like to add: ") # user asked to input data for first column
        # user is asked if they want to input data for the table's second column
        column_2 = input(f"Would you like to input data for {self.column_name[1]}? Y/N ").upper()
        if column_2 == "Y":# if yes...
            column_2_data = input("Please enter the data you'd like to add: ") # user asked to input data for second column
            # running an sql command
            table_data = self.cursor.execute(f"INSERT INTO {self.table_name} ({self.column_name[0]}, {self.column_name[1]}) VALUES ('{column_1_data}', '{column_2_data}')") # sql command to insert data input by the user (see lines 41-48) into the table they created (see line 34)

    # function to display table created by user
    def display_table(self):
        # running sql query to select all entries from table
        table_rows = self.cursor.execute(f"SELECT * FROM {self.table_name}").fetchall() # using fetchall() method we can get all the data in the table
        # for loop iterates over all the entries in the table
        for records in table_rows:
            print(records) # prints data in table


test_run = PyodbcTask() # creating an instance of the PyodbcTask class
test_run.create_table() # running function to create a table
test_run.input_data() # running function to input data into created table
test_run.display_table() # running function to display data in the table
