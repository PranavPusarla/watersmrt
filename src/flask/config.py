#!/usr/bin/python3
# config.py

import os


if __name__ == "__main__":
    exit(0)

API_NAME = "WaterSMRT"
VERSIONS = [1.0]
IP = "0.0.0.0"
PORT = 80

HOME = "/"
PRIVATE_IP = os.popen('ip route').read().split('src ')[-1].split(' ')[0]
DB_FILE = "/root/PycharmProjects/watersmrt/src/data/test.db"
