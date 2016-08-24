#!/usr/bin/env python
#! --*-- coding: utf-8 --*--

import subprocess

p1 = subprocess.Popen(['uname','-sv'], stdout=subprocess.PIPE)
uname = p1.stdout.readline()
print uname

# 对str进行数据提取的内建方法
# in和not in
print 'Linux' in uname
print 'Darwin' not in uname

# find()和index
print uname.index('Linux')
print uname.find('Linux')
#uname.index('Darwin')

# 字符串切分
smp_index = uname.index('SMP')
print uname[smp_index:]
print uname[:smp_index]

# startswith()和endswith() 判断字符串是否以制定子串开始或结尾
some_string = "Raymond Linux-Yacht"
print some_string.startswith('Raymond') # 等价 some_string[len('Raymond'):] == 'Raymond'
print some_string.endswith('-Yacht') # 等价 some_string[-len('-Yacht'):] == 'Yacht'
print some_string[-len('-Yacht'):] == '-Yacht'

