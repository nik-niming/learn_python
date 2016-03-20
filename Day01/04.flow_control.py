#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'niming'

print_num = input('Which loop do you want it ti be printed out?')

count = 0

while count < 100000000:
    if count == print_num:
        print 'There you got the number:', count
        choice = raw_input('Do you want to continue the loop?(y/n)')
        if choice == 'n':
            break
        else:
            while True:
                print_num = input('Which loop do you want it ti be printed out?')
                if print_num <= count:
                    print u'已经过了，sx!'
                else:
                    break
    else:
        print 'Loop:', count

    count += 1
else:
    print 'Loop:', count