#!/usr/bin/env python

import time
import sys
import os

if len(sys.argv) != 2:
    print 'Usage: {0} <name>'.format(sys.argv[0])
    exit()

epoch_time = sys.argv[1]

filename = 'content/{0}.md'.format(epoch_time)

def remove_ignore_error(filename):
    try:
        print filename
        os.remove(filename)
    except OSError:
        pass

remove_ignore_error(filename)
remove_ignore_error('content/images/{0}.jpg'.format(epoch_time))
remove_ignore_error('content/images/small/{0}.jpg'.format(epoch_time))
remove_ignore_error('content/images/mini/{0}.jpg'.format(epoch_time))
remove_ignore_error('content/images/icon/{0}.jpg'.format(epoch_time))
