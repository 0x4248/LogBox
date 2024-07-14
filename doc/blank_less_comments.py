# LogBox
# A data logging system that logs system data to CSV files so they can be used within grafana.
# Github: https://www.github.com/0x4248/LogBox
# Licence: GNU General Public License v3.0
# By: 0x4248

INFO = {
    "name": "Blank",
    "description": "A blank script that logs every second",
    "author": "LogBox",
    "version": "1.0",
    "config_location": "blank",
    "dependencies": [],
}

CONFIG = {
    "sample_rate": 1,
    "output": "blank",
}

import time
import datetime

from lib import config
from lib import logging

def main():
    conf = config.load_config(INFO["config_location"], CONFIG)

    data = {
        "time": "",
        "value": 0,
    }

    while True:
        data["time"] = datetime.datetime.now().isoformat() + "Z"
        data["value"] = str(int(data["value"]) + 1)
        logging.insert(conf["output"], data, ["time", "value"])
        time.sleep(conf["sample_rate"])