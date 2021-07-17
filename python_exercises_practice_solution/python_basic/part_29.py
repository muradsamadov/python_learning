# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

def function(a,b,c):
    if a == b:
        return 0
    elif a == c:
        return 0
    elif b == c:
        return 0
    else:
        return a + b + c

print(function(10,5,10))


#####other solution
def sum(x, y, z):
    if x == y or y == z or x==z:
        sum = 0
    else:
        sum = x + y + z
    return sum

print(sum(2, 1, 2))
print(sum(3, 2, 2))
print(sum(2, 2, 2))
print(sum(1, 2, 3))
