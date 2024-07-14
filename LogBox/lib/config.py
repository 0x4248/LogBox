# LogBox
# A data logging system that logs system data to CSV files so they can be used within grafana.
# Github: https://www.github.com/0x4248/LogBox
# Licence: GNU General Public License v3.0
# By: 0x4248

import os
import json

def load_config(name, default):
    path = f"config/{name}.json"
    if not os.path.exists(path):
        with open(path, "w") as f:
            json.dump(default, f, indent=4)
            return default
    with open(f"config/{name}.json", "r") as f:
        return json.load(f)