#!/usr/bin/env python
#! --*-- coding: UTF-8 --*--

import httplib
import sys

def check_webserver(address, port, resource):
    # create connection
    if not resource.startwith('/'):
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
    except:
        psass
