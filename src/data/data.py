#!/usr/bin/python3
# data.py

import os
import matplotlib.pyplot as plt


def weekly(last_week, this_week):
    x = [0, 1, 2, 3, 4, 5, 6]
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


def total(gallons):
    weeks = range(len(gallons))
    plt.plot(gallons, "bo")
    plt.plot(weeks, gallons, "b")
    plt.xticks(weeks, ["Week " + str(x + 1) for x in weeks])
    plt.xlabel("Weeks")
    plt.ylabel("Gallons")
    plt.title("Total")
    plt.savefig(os.path.join(os.path.abspath(__file__).split("/data/")[-2], "flask", "static", "graphs", "total.png"))


#weekly([2, 4, 1, 5, 7, 3, 6], [3, 5, 6, 8, 6, 4, 7])
total([2, 4, 1, 5, 7, 3, 6])
