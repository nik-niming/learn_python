#!/usr/bin/env python
# --*-- coding: UTF-8 --*--

import sys, os

def daemonize(stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
    # 执行第一次fork
    try:
        pid = os.fork()
        if pid > 0: # 父进程
            sys.exit(0) # 脱离父进程
    except OSError, e:
        sys.stderr.write("fork #1 failed: (%d) %s\n" % (e.errno, e.strerror))
        sys.exit(1)

    # 父进程环境分离
    os.chdir('/')
    os.umask(0)
    os.setsid() # 创建新的会话，实现不再控制终端

    # 执行第二次fork并脱离父进程
    try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0)
    except OSError, e:
        sys.stderr.write("fork #2 failed: (%d) %s\n" % (e.errno, e.strerror))

    # 现在进程处于驻守状态,重定向进程标准文件描述符(stdin,stdout,stderr)
    for f in sys.stdout, sys.stderr:
        f.flush()

    si = file(stdin, 'r')
    so = file(stdout, 'a+')
    se = file(stderr, 'a+', 0)
    os.dup2(si.fileno(), sys.stdin.fileno())
    os.dup2(so.fileno(), sys.stdout.fileno())
    os.dup2(se.fileno(), sys.stderr.fileno())
