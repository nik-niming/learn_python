#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'niming'

import sys

retry_limit = 3
retry_count = 0

lock_file_path = 'account_lock.txt'
lock_file = file(lock_file_path) #打开帐号lock文件

account_file_path = 'accounts.txt'
account_file = file(account_file_path, 'rb') #打开帐号文件

while retry_count < retry_limit: #只要重试不超过3次就不断循环
    user_name_input = raw_input('\033[32;1mUsername:\033[0m')

    for line in lock_file.readlines():
        if user_name_input in line:
            lock_file.close()
            sys.exit('\033[31;1mUser %s is locked!\033[0m' % user_name_input) #如果lock了就直接退出

    password_input = raw_input('\033[32;1mPassword:\033[0m')

    match_flag = False #默认为False,如果用户名/密码对应上，就设置为True
    for line in account_file.readlines():
        user_name,user_pwd = line.strip('\n').split() #去掉每行多余的\n,并把这一行按空格分成2列

        if user_name == user_name_input and user_pwd == password_input: #判断用户名/密码是否相等
            print 'Match!'
            match_flag = True
            print 'You are log in.'
            break
    if match_flag == True:
        break
    else:
        retry_count += 1
        print 'Username/Password not match!'
        print 'You have \033[31;1m%s\033[0m times to try.' % (retry_limit - retry_count)
else:
    if not lock_file.closed:
        lock_file.close()
    lock_file = file(lock_file_path,'ab')
    lock_file.write(user_name_input)
    lock_file.close()
    print '\033[31;1mYour account have been locked! Please contact administrator for help.\033[0m'

if not account_file.closed:
    account_file.close()

