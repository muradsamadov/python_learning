# Write a Python program to get a string which is n (non-negative integer) copies of a given string.

def function(word, n):
    result = ""
    for i in range(n):
        result = result + word
    return result

print(function('abc',3))

