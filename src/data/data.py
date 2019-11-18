#!/usr/bin/python3
# data.py

import os
import matplotlib.pyplot as plt
from datetime import datetime
from data.database import Database


def weekly_graph(last_week, this_week):
    x = range(len(last_week))
    plt.plot(x, last_week, "bo")
    plt.plot(x, this_week, "ro")
    plt.plot(x, last_week, "b", label="Last Week")
    plt.plot(x, this_week, "r", label="This Week")
    plt.legend()
    plt.xticks(x, ["S", "M", "T", "W", "T", "F", "S"])
    plt.xlabel("Days")
    plt.ylabel("Gallons")
    plt.title("Weekly")
    plt.savefig(os.path.join(os.path.abspath(__file__).split("/data/")[-2], "flask", "static", "graphs", "weekly.png"))


def total_graph(gallons):
    weeks = range(len(gallons))
    plt.plot(gallons, "bo")
    plt.plot(weeks, gallons, "b")
    plt.xticks(weeks, ["Week " + str(x + 1) for x in weeks])
    plt.xlabel("Weeks")
    plt.ylabel("Gallons")
    plt.title("Total")
    plt.savefig(os.path.join(os.path.abspath(__file__).split("/data/")[-2], "flask", "static", "graphs", "total.png"))


def total_water_time(db_file, table):
    database = Database(db_file)
    if not database.table_exists(table):
        database.close()
        return None
    query_response = database.query("SELECT timestamp FROM " + table + " ORDER BY timestamp DESC;")
    database.close()
    return [x[0] for x in query_response]


def total_water(db_file, table):
    database = Database(db_file)
    if not database.table_exists(table):
        database.close()
        return None
    query_response = database.query("SELECT total FROM " + table + " ORDER BY total DESC;")
    database.close()
    return query_response[0][0]


def total_week_water(db_file, table):
    database = Database(db_file)
    if not database.table_exists(table):
        database.close()
        return None
    query_response = database.query("SELECT timestamp, total FROM " + table + " ORDER BY timestamp ASC;")
    database.close()
    for i in range(len(query_response)):
        if is_this_week(query_response[i][0]):
            if i == 0:
                return query_response[-1][1]
            return query_response[-1][1] - query_response[i][1]
    return 0


def total_week_water2(db_file, table):
    database = Database(db_file)
    if not database.table_exists(table):
        database.close()
        return None
    query_response = database.query("SELECT timestamp, total FROM " + table + " ORDER BY timestamp ASC;")
    database.close()
    weeks = [0]
    for i in range(len(query_response)):
        if not is_same_week(query_response[i][0], query_response[weeks[-1]][0]):
            weeks[-1] = query_response[i-1][1] - query_response[weeks[-1]][1]
            weeks.append(i)
            if i == len(query_response) - 1:
                weeks.append(query_response[i][1] - query_response[i-1][1])
                break
        if i == len(query_response):
            weeks[-1] = query_response[i][1] - query_response[weeks[-1]][1]
    return weeks


def total_day_water(db_file, table, date):
    database = Database(db_file)
    if not database.table_exists(table):
        database.close()
        return None
    query_response = database.query("SELECT timestamp, total FROM " + table + " ORDER BY timestamp ASC;")
    database.close()
    start_index = 0
    end_index = -1
    flag = False
    for i in range(len(query_response)):
        if datetime.fromtimestamp(query_response[i][0]).date() == date and not flag:
            start_index = i
            flag = True
        elif datetime.fromtimestamp(query_response[i][0]).date() != date and flag:
            end_index = i - 1
            return query_response[end_index][1] - query_response[start_index][1] if start_index != 0 else query_response[end_index][1]
    return query_response[-1][1] if flag else 0


def is_this_week(timestamp):
    time = datetime.fromtimestamp(timestamp)
    if abs(datetime.now().timestamp() - timestamp) <= 604800 and get_day(time.timestamp()) >= 0 and get_day(time.timestamp()) <= get_day(datetime.now().timestamp()):
        return True
    return False


def is_same_week(timestamp1, timestamp2):
    print(abs(timestamp2 - timestamp1))
    print(get_day(timestamp1))
    print(get_day(timestamp2))
    print(timestamp1)
    print(timestamp2)
    if abs(timestamp2 - timestamp1) <= 604800 and (get_day(timestamp1) >= get_day(timestamp2) and timestamp1 >= timestamp2) or (get_day(timestamp1) <= get_day(timestamp2) and timestamp1 <= timestamp2):
        return True
    return False


def get_day(timestamp):
    time = datetime.fromtimestamp(timestamp)
    return time.weekday() + 1 if time.weekday() != 6 else 0


#weekly_graph([2, 4, 1, 5, 7, 3, 6], [3, 5, 6, 8, 6, 4, 7])
#total_graph([2, 4, 1, 5, 7, 3, 6])
#timestamps = total_water_time("test.db", "user")
#print(timestamps)
#times = [timestamps[0]]
#for i in range(len(timestamps) - 1):
#    if abs(timestamps[i] - timestamps[i+1]) > 4000:
#        times[-1] = times[-1] - timestamps[i]
#        times.append(timestamps[i+1])
#    elif i == len(timestamps) - 2:
#        times[-1] = times[-1] - timestamps[i+1]
#print(times)
#print(total_week_water("test.db", "user"))
#print(is_same_week(datetime(2019, 11, 16).timestamp(), datetime(2019, 11, 17).timestamp()))
#weekly_graph([93, 92, 103, 104, 100, 96, 98], [83, 85, 89, 94, 87, 80, 95])
#print(is_same_week(datetime.now().timestamp(), datetime(2019, 11, 16).timestamp()))