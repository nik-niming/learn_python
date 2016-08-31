#!/usr/bin/env python
# --*-- coding: UTF-8 --*--

from process_daemonizer import daemonize
import time
import sys

def mod_5_watcher():
    start_time = time.time()
    end_time = start_time + 20

    while time.time() < end_time:
        now = time.time()
        if int(now) % 5 == 0:
            sys.stderr.write("Mod 5 at %s\n" % now)
        else:
            sys.stdout.write("No Mod 5 at %s\n" % now)
        time.sleep(1)

if __name__ == '__main__':
    daemonize(stdout='/tmp/mod5_stdout.log', stderr='/tmp/mod5_stderr.log')
    mod_5_watcher()
