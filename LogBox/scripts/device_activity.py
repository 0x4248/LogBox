# LogBox
# A data logging system that logs system data to CSV files so they can be used within grafana.
# Github: https://www.github.com/0x4248/LogBox
# Licence: GNU General Public License v3.0
# By: 0x4248

INFO = {
    "name": "Device activity",
    "description": "Logs CPU, Each CPU core, Memory, Swap, Network",
    "author": "LogBox",
    "version": "1.0",
    "config_location": "device_activity",
    "dependencies": ["psutil"],
}

CONFIG = {
    "sample_rate": 1,
    "output": "device_activity",
}

import time
import datetime
import psutil
from lib import config
from lib import logging

def main():
    conf = config.load_config(INFO["config_location"], CONFIG)
    while True:
        data = {
            "time": datetime.datetime.now().isoformat() + "Z",
            "cpu": psutil.cpu_percent(),
            "memory": psutil.virtual_memory().percent,
            "swap": psutil.swap_memory().percent,
        }
        logging.insert(conf["output"], data, ["time", "cpu", "memory", "swap"])
        time.sleep(conf["sample_rate"])