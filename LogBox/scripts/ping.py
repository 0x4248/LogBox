# LogBox
# A data logging system that logs system data to CSV files so they can be used within grafana.
# Github: https://www.github.com/0x4248/LogBox
# Licence: GNU General Public License v3.0
# By: 0x4248

INFO = {
    "name": "Ping metrics",
    "description": "Pings 1.1.1.1 and logs the latency",
    "author": "LogBox",
    "version": "1.0",
    "config_location": "ping",
    "dependencies": [],
}

CONFIG = {
    "sample_rate": 1,
    "output": "ping",
    "output_2": "ping_loss_event",
    "host": "1.1.1.1"
}

import time
import datetime
from lib import logging
import subprocess

def main():
    while True:
        try:
            output = subprocess.check_output(["ping", "-c", "1", CONFIG["host"]])
            latency = output.decode().split("time=")[1].split()[0]
        except Exception as e:
            latency = None
        data = {
            "time": datetime.datetime.now().isoformat() + "Z",
            "latency": latency,
        }
        ping_loss = "Loss detected" if latency is None else "No loss"
        ping_loss_binary = 1 if latency is None else 0
        logging.insert(CONFIG["output_2"], {"time": datetime.datetime.now().isoformat() + "Z", "ping_loss": ping_loss_binary}, ["time", "ping_loss_binary"])
        logging.insert(CONFIG["output"], data, ["time", "latency"])
        if latency == None:
            pass
        else:
            time.sleep(CONFIG["sample_rate"])