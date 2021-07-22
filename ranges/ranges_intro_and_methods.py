#Ranges - unlike in Python 2, where the range() function returned a list, in Python 3 it returns an iterator; cannot be sliced
r = range(10)   #defining a range
 
print(list(r)) #converting a range to a list
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  #the result
 
print(list(r)[2:5])    #slicing a range by using the list() function first
[2, 3, 4]   #the result