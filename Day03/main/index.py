#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'niming'

import random
import hashlib
import pickle
import json

'''
# random 用于申城随机数
print random.random()
print random.randint(1,5)
print random.randrange(1,5)
'''

'''
# 生成一个随机字母
temp = random.randint(65, 90)
print chr(temp)

# 生成5位随机验证码
captch = []
for i in range(5):
    if i == random.randint(0, 5):
        captch.append(str(random.randint(0, 9)))
    else:
        captch.append(chr(random.randint(65, 90)))
print ''.join(captch)
'''

'''
# MD5加密
hash = hashlib.md5()
hash.update('admin')
print hash.hexdigest()
'''

'''
# 序列化pickle
li = ['alex', 11, 22, 'ok']

obj = pickle.dumps(li) # 以字符串形式序列化
print type(obj)
print obj

new_li = pickle.loads(obj) # 以字符串形式反序列化
print type(new_li)
print new_li

pickle.dump(li, open('data.pk', 'w')) # 以文件方式序列化
new_li = pickle.load(open('data.pk', 'r'))
print type(new_li)
print new_li
'''

'''
# 序列化json
users = [{'name': 'Tom', 'age': 30}, {'name': 'Jack', 'age': 41}]
user_json = json.dumps(users)
print type(user_json)
print user_json

json.dump(users, open('users.json', 'w'))
new_users= json.load(open('users.json', 'r'))
print type(new_users)
print new_users
'''


