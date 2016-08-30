#!/usr/bin/env python
# --*-- coding: UTF-8 --*--

import subprocess
import re

re_obj = re.compile(r'(.*?)alive')
p=subprocess.Popen('python process_ping.py', shell=True, stdout=subprocess.PIPE)

out=p.stdout.readlines()

for line in out:
    str = line.strip()
    if re_obj.search(str):
        print str
