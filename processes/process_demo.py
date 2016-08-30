#!/usr/bin/env python
# --*-- coding: UTF-8 --*--

from multiprocessing import Process, Queue
import time

q = Queue()

def f(q):
    x = q.get()
    print "Process number %s, sleeps for %s seconds" % (x, x)
    time.sleep(x)
    print "Process number %s finished" % x

for i in range(5):
    q.put(i)
    p = Process(target=f, args=[q])
    p.start()

print "Main process joins on queue"
p.join()
print "Main process finished"
