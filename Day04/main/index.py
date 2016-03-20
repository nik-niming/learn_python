#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'niming'


'''
# 反射动态加载模块,动态执行模块内的方法 (同一个包内)
str1 = 'demo'
str2 = 'foo'

module = __import__(str1)
func = getattr(module, str2)
func()
'''

# 反射动态加载模块,动态执行模块内的方法 (不同包内)
# 用户输入地址格式样例:
# Day04.reflect.backend.account/login
# Day04.reflect.backend.account/logout
data = raw_input('请输入地址:')
array = data.split('/')

module = __import__(array[0], fromlist=['account'])  # 等价于from Day04.reflect.backend import account

print module
func = getattr(module, array[1])
func()

