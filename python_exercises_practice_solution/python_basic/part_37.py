#  Write a python program to call an external command in Python.

import os

print(os.system('ls -la'))

#####solution-2
from subprocess import call

call(["ls", "-l"])