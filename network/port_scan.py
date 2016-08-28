#!/usr/bin/python
# -*- coding: utf-8 -*-

# port_scan.py <host> <start_port>-<end-port>

import sys
from socket import *

host = sys.argv[1]
portstr = sys.argv[2].split('-')

start_port = int(portstr[0])
end_port = int(portstr[1])

target_ip = gethostbyname(host)


opened_ports = []

for port in range(start_port, end_port):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.settimeout(10)
    result = sock.connect_ex((target_ip,port))


print("Opened ports:")

for i in opened_ports:
    print(i)

