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
'''

'''
# 无参数装饰器
def outer(func):
    def wrapper(arg1, arg2):
        rest = func(arg1, arg2)
        if rest > 10:
            print 'Bingo'
        else:
            print 'Ops'
        return rest
    return wrapper

@outer
def func1(x, y):
    return x + y

print func1(3, 5)
'''

'''
# 参数装饰器
def filter(before_func, after_func):
    def dec_func(func):
        def wrapper(*args, **kwargs):
            before_rest = before_func(*args, **kwargs)
            print before_rest

            main_rest = func(*args, **kwargs)
            if main_rest:
                return main_rest

            after_rest = after_func(*args, **kwargs)
            if after_rest:
                return after_rest
        return wrapper
    return dec_func


def do_before(*args, **kwargs):
    print 'invoke do before'


def do_after(*args, **kwargs):
    print 'invoke do after'


@filter(do_before, do_after)
def func1(x, y):
    return x + y

print func1(1, 2)
'''

