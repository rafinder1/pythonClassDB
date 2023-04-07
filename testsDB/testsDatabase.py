import unittest
from project_DB.class_database import Database


class TestsDatabase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('starting')
        cls.employee_db = Database(database_name='employee')

        sql_table = ''' CREATE TABLE IF NOT EXISTS employee (
                                                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                                        first_name TEXT,
                                                        last_name TEXT,
                                                        salary INTEGER
                                                    ); '''
        cls.employee_db.create_table(sql_table)

        data = [
            (None, "John", "Kowalski", 3600),
            (None, "Eleonora", "Nowak", 2950),
            (None, "Jan", "Smith", 4200),
        ]
        cls.employee_db.insert_data(table='employee', data=data)

    def test_insert_data_to_table_employee(self):
        data = [
            (None, "Eustachy", "Nowicki", 3600)
        ]
        self.employee_db.insert_data(table='employee', data=data)

        cursor = self.employee_db.con.cursor()
        cursor.execute("""SELECT * FROM employee""")

        expected = [
            (1, "John", "Kowalski", 3600),
            (2, "Eleonora", "Nowak", 2950),
            (3, "Jan", "Smith", 4200),
            (4, "Eustachy", "Nowicki", 3600)
        ]
        self.assertEqual(list(cursor), expected)

    def test_fetch_all_data_from_table_employee(self):
        cursor = self.employee_db.con.cursor()
        cursor.execute("""SELECT * FROM employee""")

        expected = [
            (1, "John", "Kowalski", 3600),
            (2, "Eleonora", "Nowak", 2950),
            (3, "Jan", "Smith", 4200)
        ]
        self.assertEqual(list(cursor), expected)
