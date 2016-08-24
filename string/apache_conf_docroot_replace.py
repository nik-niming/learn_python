#/usr/bin/env python
# -*- coding: utf8 -*—

from cStringIO import StringIO
import re

re_vhost_start = re.compile(r'<VirtualHost\s+(.*?)>')
re_vhost_end = re.compile(r'</VirtualHost>')
re_docroot = re.compile(r'(DocumentRoot\s+)(\S+)')

def replace_docroot(conf_string, vhost, new_docroot):
    conf_file = StringIO(conf_string)
    in_vhost = False
    curr_host = None

    for line in conf_file:
        vhost_start_match = re_vhost_start.search(line)
        if vhost_start_match:
            curr_host = vhost_start_match.groups()[0]
            in_vhost = True
        if in_vhost and (curr_host == vhost):
            docroot_match = re_docroot.search(line)
            if docroot_match:
                sub_line = re_docroot.sub(r'\1%s' % new_docroot, line)
                line = sub_line
        vhost_end_match = re_vhost_end.search(line)
        if vhost_end_match:
            in_vhost = False
        yield line

if __name__ == '__main__':
    import sys
    conf_file = sys.argv[1]
    vhost = sys.argv[2]
    docroot = sys.argv[3]
    conf_string = open(conf_file).read()
    for line in replace_docroot(conf_string, vhost, docroot):
        print line

