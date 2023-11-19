#!/usr/bin/env python3
import subprocess
commands = [
    "cd ~/dalle-web-ui",
    #"source dalle_3.8/bin/activate",
    'open -a "Google Chrome" "http://127.0.0.1:5000"',
    "python3 app.py",
]
for cmd in commands:
    subprocess.run(cmd, shell=True, check=True)
