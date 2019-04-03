#!/bin/bash/env python
# -*- coding: utf-8 -*-

print('I\'m ok.')

# 如果字符串里面有很多字符都需要转义，就需要加很多\，为了简化，Python还允许用r''表示''内部的字符串默认不转义
print('\\\t\\')

# 如果字符串内部有很多换行，用\n写在一行里不好阅读，为了简化，Python允许用'''...'''的格式表示多行内容
print('''line1
    line2
line3''')

# 多行字符串'''...'''还可以在前面加上r使用
print(r'''hello,\n
world''')

a = 'ABC'
b = a
a = 'XYZ'
print(b)

# 在Python中，通常用全部大写的变量名表示常量,Python根本没有任何机制保证PI不会被改变，所以，用全部大写的变量名表示常量只是一个习惯上的用法
PI = 3.14159265359

# 两种除法
print(10 / 3)
print(10 // 3)

# 余数运算
print(10 % 3)

# 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
print(ord('A'))
print(ord('中'))
print(chr(25991))

# 如果知道字符的整数编码，还可以用十六进制这么写str
print('\u4e2d\u6587')

# Python对bytes类型的数据用带b前缀的单引号或双引号表示
x = b'ABC'

# 以Unicode表示的str通过encode()方法可以编码为指定的bytes
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))

# 如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

# 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))

# len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数
print(len('中文'))
print(len('中文'.encode('utf-8')))

# 字符串格式化输出。%运算符就是用来格式化字符串的。在字符串内部，%s表示用字符串替换，%d表示用整数替换，有几个%?占位符，
# 后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

# 有些时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%
print('growth rate: %d%%' % 7)

# 字符串的format()方法，它会用传入的参数依次替换字符串内的占位符{0}、{1}……，不过这种方式写起来比%要麻烦得多
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))


