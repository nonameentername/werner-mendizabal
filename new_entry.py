#!/usr/bin/env python

import time
import sys
import os

from shutil import copyfile
from time import gmtime, strftime

if len(sys.argv) != 2:
    print 'Usage: {0} <name>'.format(sys.argv[0])
    exit()

image_filename = sys.argv[1]

epoch_time = int(time.time())

filename = 'content/{0}.md'.format(epoch_time)

output = open(filename, 'wb')

date = strftime("%Y-%m-%d", gmtime())
time = strftime("%H:%M:%S", gmtime())

output.write(
"""title: Everyday - {1}
Date: {1} {2}
Category: Art
Tags: Everyday, Art, Drawing, Krita
picture: {0}.jpg
""".format(epoch_time, date, time))

output.close()

print filename

base_filename = os.path.basename(image_filename)
base_filename = epoch_time

copyfile(image_filename, 'content/images/{0}.jpg'.format(epoch_time))
