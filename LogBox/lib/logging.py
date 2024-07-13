# LogBox
# A data logging system that logs system data to CSV files so they can be used within grafana.
# Github: https://www.github.com/0x4248/LogBox
# Licence: GNU General Public License v3.0
# By: 0x4248

import csv
import os

root = "data"

def insert(location, object, fieldnames):
    file = os.path.join(root, location + ".csv")
    if not os.path.exists(file):
        with open(file, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames)
            writer.writeheader()

    with open(file, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames)
        writer.writerow(object)
    return
