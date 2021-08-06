# Write a Python program to sum all the items in a list.

def function(items):
    sum_number = 0
    for i in items:
        sum_number += i
    return sum_number

print(function([1,2,3]))