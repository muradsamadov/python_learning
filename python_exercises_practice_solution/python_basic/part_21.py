# Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2

def function(str,n):
    result = ""
    for i in range(n):
        if str[:2] >= 2:
            result = result + str
    return result

print(function("murad",3))
