# Write a Python program to multiply all the items in a list.

def function(items):
    multiply_numbers = 1
    for i in items:
        multiply_numbers = multiply_numbers * i
    return multiply_numbers

print(function([2,3,4]))