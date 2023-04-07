import sqlite3


class Database:

    def __init__(self, database_name):
        # Connection with DB in sqlite and get cursor
        self.con = sqlite3.connect(':memory:')
        self.cur = self.con.cursor()

    def create_table(self, sql_table: str):
        self.cur.execute(sql_table)
        self.con.commit()

    def insert_data(self, table, data):
        self.cur.executemany(f"INSERT INTO {table} VALUES({','.join(['?' for _ in data[0]])})", data)
        self.con.commit()

    def fatch_all(self, table):
        return self.cur.execute(f"SELECT * FROM {table}").fetchall()
