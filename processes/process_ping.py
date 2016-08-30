#!/usr/bin/env python
# --*-- coding: UTF-8 --*--

from IPy import IP
from  multiprocessing import Process, Queue, Pool
import time
import subprocess
import sys

ip_queue = Queue()
process_list = []

ips = IP("192.168.0.0/24")

for ip in ips:
    ip_queue.put(ip)

def ping_func(i, ip_queue):
    while True:
        if ip_queue.empty():
            sys.exit(0)

        print "Process Number: %s" % i
        ip = ip_queue.get()

        ret = subprocess.call("ping -c 1 %s" % ip, shell=True,
                              stdout=open('/dev/null', 'w'),
                              stderr=subprocess.STDOUT)

        if ret == 0:
            print "%s: is alive" % ip
        else:
            print "Process Number: %s didn't find a response for %s " % (i, ip)

for i in range(10):
    p = Process(target=ping_func, args=[i,ip_queue])
    process_list.append(p)
    p.start()

# 检查生成的子进程列表，等待每个子进程结束后，主(父)进程结束
end_flag = 1

while True:
    for p in process_list:
        if p.is_alive():
            time.sleep(2)
            end_flag = 0
    if end_flag:
        break
    else:
        end_flag = 1
print "Main process finished"
sys.exit(0)
