import pyodbc

class PyodbcTask:

    def __init__(self):
        self.server = "databases1.spartaglobal.academy"
        self.database = "Northwind"
        self.username = "**"
        self.password = "*****"
        self.northwind_connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password)
        # server name - database name - username and password is required to connect to pyodbc
        self.cursor = self.northwind_connection.cursor()
        # self.cursor.execute("SELECT @@VERSION")
        # self.row = self.cursor.fetchone()
        # print(self.row)

    def create_table(self):
        self.table_name = input("Enter the table name: ")
        self.table_columns = {}
        while not "end":
            self.table_columns[input("enter column name. once finished, please enter end\n")] = input("enter datatype and any contraints")

        table = self.cursor.execute(
            f"CREATE TABLE {self.table_name} ("
            (for key, value in self.table_columns.items():
            print(f"{key}  {value},")
        )

