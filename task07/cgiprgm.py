#!/usr/bin/python3

import cgi
import subprocess as ss
import time
print("content-type: text/html")
print()

f = cgi.FieldStorage()
cmd = f.getvalue("x")
display = ss.getoutput("sudo " + cmd)
print(display)