# Write a Python program to count the number 4 in a given list.

def function(numbers):
    count = 0
    for i in numbers:
        if i == 4:
            count = count + 1
    return count

print(function([1,2,3,4,5,6,4,4]))