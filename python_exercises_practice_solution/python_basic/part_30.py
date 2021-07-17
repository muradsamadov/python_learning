# Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.

def function(a,b):
    sum = a + b
    if sum in range(15,21):
        return 20
    else:
        return sum

print(sum(10, 6))
print(sum(10, 2))
print(sum(10, 12))