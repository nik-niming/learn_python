#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'niming'

import sys,os

if len(sys.argv) < 4:
    print "usage:./file_replace.py old_text new_test filename"

old_text, new_text = sys.argv[1],sys.argv[2]
file_name = sys.argv[3]

f = file(file_name,'rb')
tmp_file = file('%s.tmp' % file_name,'wb') #tmp file for writting
for line in f.xreadlines(): # loop old file and replace the old text to new text
    tmp_file.write(line.replace(old_text,new_text))

f.close()
tmp_file.close()

if '--bak' in sys.argv:
    os.rename(file_name, '%s.bak' % file_name)
    os.rename('%s.tmp' % file_name, file_name)
else:
    os.rename('%s.tmp' % file_name, file_name)
