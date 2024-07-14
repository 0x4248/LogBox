# LogBox
# A data logging system that logs system data to CSV files so they can be used within grafana.
# Github: https://www.github.com/0x4248/LogBox
# Licence: GNU General Public License v3.0
# By: 0x4248
#
# This is a blank script that logs every second

# Basic information about the script
INFO = {
    "name": "Blank",
    "description": "A blank script that logs every second",
    "author": "LogBox",
    "version": "1.0",
    "config_location": "blank",
    "dependencies": [],
}

# Default configuration
CONFIG = {
    # How long to sleep for
    "sample_rate": 1,
    # The output file
    "output": "blank",
}

# Import needed modules for time logging and sleeping
import time
import datetime

# Import LogBox modules
from lib import config
from lib import logging

def main():
    # Load the configuration
    conf = config.load_config(INFO["config_location"], CONFIG)

    # Output data structure
    data = {
        "time": "",
        "value": 0,
    }

    while True:
        # Update the time and value
        data["time"] = datetime.datetime.now().isoformat() + "Z"
        data["value"] = str(int(data["value"]) + 1)
        
        # Insert the data into the output file
        logging.insert(conf["output"], data, ["time", "value"])
        
        # Sleep for the sample rate
        time.sleep(conf["sample_rate"])