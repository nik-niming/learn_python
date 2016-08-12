#!/usr/bin/env python

#A system information gathering script

import subprocess

#command 1
def uname_func():
    uname = "uname"
    uname_arg = "-a"
    print("Gathering system information with {0} command".format(uname))
    subprocess.call([uname,uname_arg])

#command 2
def df_func():
    diskspace = "df"
    diskspace_arg = "-h"
    print("Gathering disk information with {0} command".format(diskspace))
    subprocess.call([diskspace,diskspace_arg])

def main():
    uname_func()
    df_func()

main()
