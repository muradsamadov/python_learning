# Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum. 

def function(a, b, c):
    sum = (a + b + c)

    if a == b == c:
        return sum * 3
    else:
        return sum

print(function(1,1,1))