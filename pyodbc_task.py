import pyodbc

class PyodbcTask:

    def __init__(self):
        self.server = "databases1.spartaglobal.academy"
        self.database = "Northwind"
        self.username = "SA"
        self.password = "Passw0rd2018"
        self.northwind_connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password)
        # server name - database name - username and password is required to connect to pyodbc
        self.cursor = self.northwind_connection.cursor()
        # self.cursor.execute("SELECT @@VERSION")
        # self.row = self.cursor.fetchone()
        # print(self.row)
        self.table_name = ""
        self.column_name = []
        self.column_datatype = []


    def create_table(self):
        self.table_name = input("Enter the table name: ")

        i = 1
        while i < 3:
            self.column_name.append(input(f"Please enter the name of column {i}: "))
            self.column_datatype.append(input(f"Please enter the datatype of column {i}: ").upper())
            i += 1

        table = self.cursor.execute(
            f"CREATE TABLE {self.table_name} ( {self.column_name[0]} {self.column_datatype[0]}, {self.column_name[1]} {self.column_datatype[1]} )")
        return table

    def input_data(self):
        column_1 = input(f"Would you like to input data for {self.column_name[0]}? Y/N ").upper()
        if column_1 == "Y":
            column_1_data = input("Please enter the data you'd like to add: ")
            table_data = self.cursor.execute(f"INSERT INTO {self.table_name} ({self.column_name[0]}) VALUES ({column_1_data});")

        column_2 = input(f"Would you like to input data for {self.column_name[1]}? Y/N" ).upper()
        if column_2 == "Y":
            column_2_data = input("Please enter the data you'd like to add:")
            table_data_2 = self.cursor.execute(f"INSERT INTO {self.table_name} ({self.column_name[1]}) VALUES ({column_2_data});")

    def display_table(self):
        table_rows = self.cursor.execute(f"SELECT * FROM {self.table_name}").fetchall()
        for records in table_rows:
            print(records)


test_run = PyodbcTask()
test_run.create_table()
test_run.input_data()
