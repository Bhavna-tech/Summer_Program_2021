#!/usr/bin/python3

import subprocess 
import cgi
import time

print("content-type: text/html")
print()

requirement = cgi.FieldStorage()

cmd = requirement.getvalue("command")

output = subprocess.getoutput("sudo " +cmd+ " --kubeconfig /root/kubews/admin.conf") 

print(output)
