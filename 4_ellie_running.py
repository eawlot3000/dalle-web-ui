#!/usr/bin/env python3
import subprocess
import time
commands = [
    "cd ~/dalle-web-ui",
    "python3 -m venv dalle_3.8 && source dalle_3.8/bin/activate",
    "python3 app.py",
]

time.sleep(3)
for cmd in commands:
    subprocess.run(cmd, shell=True, check=True)

chrome_cmd = 'open -a "Google Chrome" "http://127.0.0.1:5000"'
subprocess.run(chrome_cmd, shell=True)
