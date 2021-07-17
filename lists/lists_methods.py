#Lists - methods
list2 = [-11, 2, 12]

print(min(list2)) #returns the smallest element (value) in the list

print(max(list2)) #returns the largest element (value) in the list

list1 = ["Cisco", "Juniper", "Avaya", 10, 10.5, -11]

list1.append(100) #appending a new element to the list

print(list1)

del list1[4] #removing an element from the list by index

print(list1)

list1.pop(0) #removing an element from the list by index

print(list1)

list1.remove("Juniper") #removing an element from the list by value

print(list1)

list1.insert(2, "Nortel") #inserting an element at a particular index

print(list1)

list1.extend(list2) #appending a list to another list

print(list1)

print(list1.index(-11)) #returns the index of element -11

print(list1.count(10)) #returns the number of times element 10 is in the list


list2 = [9, 99, 999, 1, 25, 500]

list2.sort() #sorts the list elements in ascending order; modifies the list in place

print(list2)

list2.reverse() #reverses the elements of the list

print(list2)

x = sorted(list2) #sorts the elements of a list in ascending order and creates a new list at the same time

print(x)

print(list1 + list2) #concatenating two lists

print(list1*3) #repetition of a list