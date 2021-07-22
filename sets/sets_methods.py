#Sets - methods
set1 = {1,2,3,4}
set2 = {3,5,8}

print(set1.intersection(set2)) #returns the common elements of the two sets

print(set2.intersection(set1))

print(set1.difference(set2)) #returns the elements that set1 has and set2 doesn't

print(set2.difference(set1))

print(set1.union(set2)) #unifying two sets; the result is also a set, so there are no duplicate elements; not to be confused with concatenation

print(set1.pop()) #removes a random element from the set; set elements cannot be removed by index because sets are UNORDERED collections of elements, so there are no indexes to use

print(set1)

set1.clear() #clearing a set; the result is an empty set

print(set1)