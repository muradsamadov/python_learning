# Write a Python function that takes two lists and returns True if they have at least one common member.

def function(list1, list2):
    result = False
    for x in list1:
        for y in list2:
            if x == y:
                result = True
                return result

print(function([1,2,3,4,5], [5,6,7,8,9]))
print(function([1,2,3,4,5], [6,7,8,9]))