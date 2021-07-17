# Write a Python program to check whether a specified value is contained in a group of values.

def function(group_data,number):
    if number in group_data:
        return True
    else:
        return False

print(function([1,2,3], 4))

#####another solution
def is_group_member(group_data, n):
   for value in group_data:
       if n == value:
           return True
   return False
print(is_group_member([1, 5, 8, 3], 3))
print(is_group_member([5, 8, 3], -1))



