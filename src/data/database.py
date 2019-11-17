#!/usr/bin/python3
# database.py

import sqlite3


class Database:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def create_database(self, db_file):
        self.cursor.execute(".open " + db_file)

    def create_table(self, table):
        self.cursor.execute("CREATE TABLE " + table + " (timestamp timestamp, rate float, total float, source text);")

    def drop_table(self, table):
        self.cursor.execute("DROP TABLE " + table + ";")

    def insert(self, table, entry):
        self.cursor.execute("INSERT INTO " + table + " (timestamp, rate, total, source) VALUES (" + "".join(entry) + ");")

    def delete(self, table, entry):
        self.cursor.execute("DELETE FROM " + table + " WHERE timestamp = " + entry[0] + ";")

    def query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()
