#  Write a python program to get the path and name of the file that is currently executing.

import os
print("Current File Name : ",os.path.realpath(__file__))
print('basename:    ', os.path.basename(__file__))
print('dirname:     ', os.path.dirname(__file__))
