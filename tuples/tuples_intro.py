#Tuples - immutable lists (their contents cannot be changed by adding, removing or replacing elements)
my_tuple = () #creating an empty tuple

print(my_tuple)

my_tuple = (9,) #creating a tuple with a single element; DO NOT forget the comma
 
print(type(my_tuple))

my_tuple = (1, 2, 3, 4)
 
#Tuples - the same indexing & slicing rules apply as for strings and lists
print(len(my_tuple)) #returns the number of elements in the tuple
 
print(my_tuple[0]) #returns the first element in the tuple (index 0)
print(my_tuple[-1]) #returns the last element in the tuple (index -1)
print(my_tuple[0:2]) #returns (1, 2)
print(my_tuple[:2]) #returns (1, 2)
print(my_tuple[1:]) #returns (2, 3, 4)
print(my_tuple[:]) #returns (1, 2, 3, 4)
print(my_tuple[:-2]) #returns (1, 2)
print(my_tuple[-2:]) #returns (3, 4)
print(my_tuple[::-1]) #returns (4, 3, 2, 1)
print(my_tuple[::2]) #returns (1, 3)
 
#Tuples - tuple assignment / packing and unpacking
tuple1 = ("Cisco", "2600", "12.4")
 
(vendor, model, ios) = tuple1 #vendor will be mapped to "Cisco" and so are the rest of the elements with their corresponding values; both tuples should have the same number of elements
 
print(vendor)
print(model)
print(ios)

(a, b, c) = (1, 2, 3) #assigning values in a tuple to variables in another tuple
 
print(a,b,c)