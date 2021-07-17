#  Write a Python program to locate Python site-packages.

import sysconfig
print(sysconfig.get_paths()["purelib"])

#####solution-2
import site; 
print(site.getsitepackages())
