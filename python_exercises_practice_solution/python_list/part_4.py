# Write a Python program to get the smallest number from a list.

def function(items):
    # number = 0
    number = items[0]
    for i in items:
        if i < number:
            number = i

    return number

print(function([2,300,76,77]))