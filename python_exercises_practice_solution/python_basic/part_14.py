# Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.

a = 5

if a <= 17:
    print(17 - a)
else:
    print((a - 17) * 2)

#####

def function(n):
    if n <= 17:
        return 17 - n
    else:
        (n - 17)*2

print(function(5))
print(function(21))