#Lists - slicing (works the same as string slicing, but with list elements instead of string characters)
a_list = [1, 2, 3, "a", "b", "c", "d", "m", "u", "r", "a", "d", 4, 5, 6, 7]

print(a_list[5:15]) #slice starting at index 5 up to, but NOT including, index 15; so index 14 represents the last element in the slice
print(a_list[5:]) #slice starting at index 5 up to the end of the list
print(a_list[:10]) #slice starting at the beginning of the list up to, but NOT including, index 10
print(a_list[:]) #returns the entire list
print(a_list[-1]) #returns the last element in the list
print(a_list[-2]) #returns the second to last element in the list
print(a_list[-9:-1]) #extracts a certain sublist using negative indexes
print(a_list[-5:]) #returns the last 5 elements in the list
print(a_list[:-5]) #returns the list minus its last 5 elements
print(a_list[::2]) #adds a third element called step; skips every second element of the list
print(a_list[::-1]) #returns a_list's elements in reverse order