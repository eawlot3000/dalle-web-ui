#!/usr/bin/env python3
import subprocess
chrome_cmd = 'open -a "Google Chrome" "http://127.0.0.1:5000"'
subprocess.run(chrome_cmd, shell=True)

