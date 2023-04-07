from sys import argv
from class_database import Database


# Initialize Database
employee_db = Database(database_name='employee')

if len(argv) == 2:
    if argv[1] == 'create':
        """
        Create table employee - column names 
        (ID: ,first_name: str, last_name:str, salary:int)
        """

        sql_table = ''' CREATE TABLE IF NOT EXISTS employee (
                                                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                                first_name TEXT,
                                                last_name TEXT,
                                                salary INTEGER
                                            ); '''
        employee_db.create_table(sql_table)

    elif argv[1] == 'insert':
        """
        Insert data to table
        """
        data = [
            (None, "John", "Kowalski", 3600),
            (None, "Eleonora", "Nowak", 2950),
            (None, "Jan", "Smith", 4200),
        ]
        employee_db.insert_data(table='employee', data=data)

    elif argv[1] == 'select':
        """
        Select data from table
        """
        print(employee_db.fatch_all(table='employee'))

else:
    pass
