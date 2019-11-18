#!/usr/bin/python3
# parse.py

import os
from database import Database


def read_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        file.close()
    timestamp = lines[0]
    timestamps = [str(float(timestamp.strip()) + float(lines[i].strip())) for i in range(1, len(lines), 4)]
    rates = [lines[i].strip() for i in range(2, len(lines), 4)]
    totals = [lines[i].strip() for i in range(3, len(lines), 4)]
    return timestamps, rates, totals


def write_to_table(db_file, table, timestamps, rates, totals, source):
    database = Database(db_file)
    if not database.table_exists(table):
        database.create_table(table)
    values = ", ".join(["(" + timestamps[i] + ", " + rates[i] + ", " + totals[i] + ", \"" + source + "\")" for i in range(len(timestamps))])
    database.query("INSERT INTO " + table + " (timestamp, rate, total, source) VALUES " + values + ";")
    database.commit()
    database.close()


filename = "faucet.txt"
source = os.path.splitext(filename)[0]
timestamps, rates, totals = read_file(filename)
write_to_table("test.db", "user", timestamps, rates, totals, source)