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

'''
class Province(object):
    memo = '类静态变量'

    def __init__(self, name, flag):
        self.name = name  # 实例变量
        self.__thailand = flag  # 私有实例变量

    def __call__(self):
        print '调用类实例的call方法'

    def sports_meet(self):  # 类实例方法
        print self.name + '正在开运动会'

    def show(self):
        print self.__thailand
        self.__foo()

    def __foo(self):
        print '实例私有方法'

    @property
    def bar(self):  # 实例属性,装饰器property将类实例方法的访问转换成对实例变量的访问
        print self.name

    @bar.setter
    def bar(self, value):  # 实例属性的写方法
        self.name = value

    @staticmethod
    def foo():  # 类静态方法
        print '静态方法'

p = Province('SC', True)
p()
p.sports_meet()

print p.memo  # 类实例可以访问类静态变量
p.foo()  # 类实例可以调用类静态方法
Province.foo()  # 直接访问类静态方法
p.bar = 'AAAAA'
print p.bar
p.show()
# Province.sports_meet()  # 类无法访问类实例方法
'''

'''
# 新式类,子类调用父类函数
class Father(object):
    def __init__(self):
        print('call Father init method.')


class Son(Father):
    def __init__(self):
        super(Son, self).__init__()
        print 'call Son init method.'

s = Son()
'''

'''
# 经典类多继承,父类方法搜索路径(左->右),但是深度优先,而不是广度优先
class A:
    def __init__(self):
        print('this is A')

    def save(self):
        print('save method from A')


class B(A):
    def __init__(self):
        print('this is B')


class C(A):
    def __init__(self):
        print('this is C')

    def save(self):
        print('save method from C')


class D(B, C):
    def __init__(self):
        print('this is D')

obj = D()
obj.save()
'''

'''
# 新式类多继承,父类方法搜索路径(左->右),是广度优先
class A(object):
    def __init__(self):
        print('this is A')

    def save(self):
        print('save method from A')


class B(A):
    def __init__(self):
        print('this is B')


class C(A):
    def __init__(self):
        print('this is C')

    def save(self):
        print('save method from C')


class D(B, C):
    def __init__(self):
        print('this is D')

obj = D()
obj.save()
'''

'''
# Python抽象类,抽象方法实现接口

from abc import ABCMeta, abstractmethod


class MessageSender:
    __metaclass__ = ABCMeta

    @abstractmethod
    def send(self, msg):
        pass


class EmailSender(MessageSender):
    def __init__(self):
        print('init Email MessageSender')

    def send(self, msg):
        print('process send message: {0}'.format(msg))


sender = EmailSender()
if isinstance(sender, MessageSender):
    sender.send('Hello world')
'''


# 自定义异常类,try...except...else...finally

class AuthError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return 'AuthorError:{}'.format(self.msg)

login_flag = 1

try:
    if login_flag == 1:
        raise AuthError('User name or password error.')
except AuthError, e:
    print e
else:
    print('no auth error')
finally:
    print('do it always')

