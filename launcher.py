#/usr/bin/env python

import os
import sys
import atexit
from subprocess import Popen

pidfile = "/tmp/remote-python-code.pid"

if os.path.isfile(pidfile):
    print("{0} already exists, exiting".format(pidfile))
    sys.exit()

pid = Popen(["python3", "main.py"]).pid
with open(pidfile, 'w') as f:
    atexit.register(lambda: os.unlink(pidfile))
    f.write(pid)
