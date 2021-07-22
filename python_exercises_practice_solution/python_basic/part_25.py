# Write a Python program to concatenate all elements in a list into a string and return it.

def function(list):
    result = ""
    for i in list:
        result = result + str(i)
    return result

print(function([1, 5, 12, 2]))