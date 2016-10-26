#!/usr/bin/env python
# --*-- coding: UTF-8 --*__

from optparse import OptionParser
import network.ftplib
import sys

parser = OptionParser()

parser.add_option("-a", "--remote_host_address", dest="remote_host_address",
                  help="Remote FTP Host", metavar="REMOTE FTP HOST")
parser.add_option("-r", "--remote_file", dest="remote_file",
                  help="Remote file name to download", metavar="REMOTE FILE NAME")
parser.add_option("-l", "--local_file", dest="local_file",
                  help="Local file name to save", metavar="LOCAL FILE NAME")
parser.add_option("-u", "--username", dest="username",
                  help="Username for FTP server", metavar="USERNAME")
parser.add_option("-p", "--password", dest="password",
                  help="Password for FTP server", metavar="USERNAME")

(options, args) = parser.parse_args()

if not (options.remote_host_address and options.remote_file and options.local_file):
    parser.error('REMOTE FTP HOST, REMOTE FILE NAME and LOCAL FILE NAME are mandatory')

if options.username and not options.password:
    parser.error('PASSWORD is mandatory if USERNAME is presen')

ftp = network.ftplib.FTP(options.remote_host_address)

if options.username:
    try:
        ftp.login(options.username, options.password)
    except network.ftplib.error_perm, e:
        print "Login failed: %s" % e
        sys.exit(1)
else:
    try:
        ftp.login()
    except network.ftplib.error_perm, e:
        print "Anonymous login failed: %s" % e
        sys.exit(1)

try:
    local_file = open(options.local_file, 'wb')
    ftp.retrbinary('RETR %s' % options.remote_file, local_file.write)
finally:
    local_file.close()
    ftp.close()
