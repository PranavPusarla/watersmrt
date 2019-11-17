#!/usr/bin/python3
# database.py

import sqlite3


class Database:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def create_database(self, db_file):
        self.cursor.execute(".open " + db_file)

    def create_table(self, table):
        self.cursor.execute("CREATE TABLE " + table + " (timestamp timestamp, rate float, total float, source text);")

    def drop_table(self, table):
        self.cursor.execute("DROP TABLE " + table + ";")

    def insert(self, table, entry):
        self.cursor.execute("INSERT INTO " + table + " (timestamp, rate, total, source) VALUES (" + ", ".join(entry) + ");")

    def delete(self, table, entry):
        self.cursor.execute("DELETE FROM " + table + " WHERE timestamp = " + entry[0] + ";")

    def query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def table_exists(self, table):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        return table in [x[0] for x in self.cursor.fetchall()]

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()
