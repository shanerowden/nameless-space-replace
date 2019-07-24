#!/usr/bin/env python3

import os
import subprocess

directories = [os.path.abspath(dir) for dir in os.listdir() if os.path.isdir(dir)]
directories.sort()

for directory in directories:
    directory = os.path.abspath(directory)
    os.chdir(directory)
    subprocess.run('nsr')
