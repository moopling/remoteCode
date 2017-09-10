#/usr/bin/env python

import os
import sys
import atexit
from test import runforever

pid = str(os.getpid())
pidfile = "/tmp/remote-python-code.pid"

if os.path.isfile(pidfile):
    print("{0} already exists, exiting".format(pidfile))
    sys.exit()

with open(pidfile, 'w') as f:
    atexit.register(lambda: os.unlink(pidfile))
    f.write(pid)

runforever()
