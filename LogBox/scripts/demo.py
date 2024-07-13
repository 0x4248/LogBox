# LogBox
# A data logging system that logs system data to CSV files so they can be used within grafana.
# Github: https://www.github.com/0x4248/LogBox
# Licence: GNU General Public License v3.0
# By: 0x4248

INFO = {
    "name": "Demo metrics",
    "description": "A simple metric that takes outputs random numbers logged every second",
    "author": "LogBox",
    "version": "1.0",
    "dependencies": [],
}

import time
import datetime
import random
from lib import logging

def main():
    while True:
        data = {
            "time": datetime.datetime.now().isoformat() + "Z",
            "value": random.randint(0, 100),
        }
        logging.insert("demo", data, ["time", "value"])
        time.sleep(1)
