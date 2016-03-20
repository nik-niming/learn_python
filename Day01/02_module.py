#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'niming'

import os
import commands
import sys


res = os.popen('pwd').read()
print res

res = commands.getstatusoutput('pwd')
print res

print sys.argv
