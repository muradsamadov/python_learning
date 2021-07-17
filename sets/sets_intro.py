#Sets - unordered collections of unique elements
list4 = [1,2,3,4,5,2,3]

print(list4)

print(set(list4)) #creating a set from a list; removing duplicate elements; returns {1,2,3,4,5}

set1 = set([11,12,13,14,15,15,15,11])

print(set1)

set2 = {11,12,13,14,15,15,15,11}

print(set2)

print(len(set2)) #returns the number of elements in the set

print(11 in set2) #returns True; checking if a value is an element of a set

print(10 in set2) #returns True; checking if a value is an element of a set

set2.add(16) #adding an element to a set

print(set2)

set2.remove(11) #removing an element from a set

print(set2)