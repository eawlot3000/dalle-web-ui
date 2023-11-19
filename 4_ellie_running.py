#!/usr/bin/env python3
import subprocess
commands = [
    'open -a "Google Chrome" "http://127.0.0.1:5000"',
    "python3 ~/dalle-web-ui/app.py",
]
for cmd in commands:
    subprocess.run(cmd, shell=True, check=True)
