#Frozensets - immutable sets. The elements of a frozenset remain the same after creation.
fs1 = frozenset(list1) #defining a frozenset
 
fs1
frozenset({11, 12, 13, 14, 15}) #the result
 
type(fs1)
<class 'frozenset'> #the result
 
#proving that frozensets are indeed immutable
fs1.add(10)
AttributeError: 'frozenset' object has no attribute 'add'
 
fs1.remove(1)
AttributeError: 'frozenset' object has no attribute 'remove'
 
fs1.pop()
AttributeError: 'frozenset' object has no attribute 'pop'
 
fs1.clear()
AttributeError: 'frozenset' object has no attribute 'clear'



#Frozensets - immutable sets. The elements of a frozenset remain the same after creation.
list1 = [1,2,3,4]
list2 = [3,4,7]

fs1 = frozenset(list1) #defining a frozenset
fs2 = frozenset(list2) #defining a frozenset

#proving that frozensets are indeed immutable
# fs1.add(10) #AttributeError: 'frozenset' object has no attribute 'add'

# print(fs1)

#others
print(fs1.intersection(fs2))

print(fs1.difference(fs2))

print(fs1.union(fs2))