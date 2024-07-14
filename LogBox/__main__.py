# LogBox
# A data logging system that logs system data to CSV files so they can be used within grafana.
# Github: https://www.github.com/0x4248/LogBox
# Licence: GNU General Public License v3.0
# By: 0x4248

import os
import sys
import threading
import importlib

from lib.colour import Colours

__MAIN__PATH = os.path.dirname(os.path.realpath(__file__))
sys.path.append(__MAIN__PATH)

def count_scripts():
    x = 0
    for root, dirs, files in os.walk(os.path.join(__MAIN__PATH, "scripts")):
        for file in files:
            if file.endswith(".py"):
                x += 1
    return x

def convert_script_to_py_path(script):
    script = script.replace("/", ".")
    return f"scripts.{script}"

def main():
    scripts = []
    for root, dirs, files in os.walk(os.path.join(__MAIN__PATH, "scripts")):
        for file in files:
            if file.endswith(".py"):
                scripts.append(file.replace(".py", ""))
    threads = []
    for script in scripts:
        print(f"{Colours.BACK_GREEN}{Colours.WHITE} SCRIPT BOOT {Colours.RESET} {script}")
        script_path = convert_script_to_py_path(script)
        script_module = importlib.import_module(script_path)
        t = threading.Thread(target=script_module.main)
        threads.append(t)
        t.start()

if __name__ == "__main__":
    main()
