#!/usr/bin/env python
#! --*-- coding = utf-8 --*--
"""
subprocess 模块使用方法
http://www.cnblogs.com/vamei/archive/2012/09/23/2698014.html
"""

import subprocess

cp1 = subprocess.Popen(['uname','-sv'],stdout=subprocess.PIPE)
cp2 = subprocess.Popen(['wc'],stdin=cp1.stdout,stdout=subprocess.PIPE)
out = cp2.communicate()
print out



