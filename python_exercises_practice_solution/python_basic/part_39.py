#  Write a Python program to find out the number of CPUs using.

import os

print(os.cpu_count())

#####solution-2

import multiprocessing

print(multiprocessing.cpu_count())
