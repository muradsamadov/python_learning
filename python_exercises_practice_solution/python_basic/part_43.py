#####
import getpass
print(getpass.getuser())


#####solution1
import subprocess

subprocess.run(["whoami"])


#####solution 2
import os

os.system("whoami")


