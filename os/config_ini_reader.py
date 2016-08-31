#!/usr/bin/env python
# --*-- coding: UTF-8 --*--

import ConfigParser

def readConfig(file="config.ini"):
    ips = []
    cmds = []

    config = ConfigParser.ConfigParser()
    config.read(file)
    machines = config.items("MACHINES")
    commands = config.items("COMMANDS")

    for ip in machines:
        ips.append(ip[1])

    for cmd in commands:
        cmds.append(cmd[1])
    return ips, cmds

if __name__ == '__main__':
    ips, cmds = readConfig()
    print ips
    print cmds
