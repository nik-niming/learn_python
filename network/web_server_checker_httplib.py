#!/usr/bin/env python
# --*-- coding: UTF-8 --*--

import httplib
import sys
import socket


def check_webserver(address, port, resource):
    # create connection
    if not resource.startswith('/'):
        resource = '/' + resource

    try:
        conn = httplib.HTTPConnection(address, port)
        print "HTTP connection created successfully"
        # make request
        req = conn.request('GET', resource)
        print "request for %s successful" % resource
        # get ressponse
        resp = conn.getresponse()
        print "response status:%s" % resp.status
    except socket.error, e:
        print "HTTP connetion failed:%s" % e
        return False
    finally:
        conn.close()
        print "HTTP connection close successfully"

    if resp.status in [200, 301]:
        return True
    else:
        return False

if __name__ == '__main__':
    from optparse import OptionParser

    parser = OptionParser()

    parser.add_option("-a", "--address", dest="address", default="localhost",
                      help="Address for web server", metavar="ADDRESS")
    parser.add_option("-p", "--port", dest="port", type="int", default="80",
                      help="Port for web server", metavar="PORT")
    parser.add_option("-r", "--resource", dest="resource", default="index.html",
                      help="Resource to check", metavar="RESOURCE")

    (options, args) = parser.parse_args()
    print "options: %s, args: %s" % (options, args)

    check = check_webserver(options.address, options.port, options.resource)
    print "check_webserver returned %s" % check
    sys.exit(not check)
