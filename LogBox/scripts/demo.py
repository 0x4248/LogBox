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
    "config_location": "demo",
    "dependencies": [],
}

CONFIG = {
    "sample_rate": 1,
    "output": "demo",
}

import time
import datetime
import random
from lib import config
from lib import logging

def main():
    conf = config.load_config(INFO["config_location"], CONFIG)
    while True:
        data = {
            "time": datetime.datetime.now().isoformat() + "Z",
            "value": random.randint(0, 100),
        }
        logging.insert(conf["output"], data, ["time", "value"])
        time.sleep(conf["sample_rate"])