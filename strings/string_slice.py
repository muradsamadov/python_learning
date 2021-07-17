#Strings - slicing
string1 = "O E2 10.110.8.9 [160/5] via 10.119.254.6, 0:01:00, Ethernet2"
 
print(string1[5:15]) #slice starting at index 5 up to, but NOT including, index 15; so index 14 represents the last element in the slice
print(string1[5:]) #slice starting at index 5 up to the end of the string
print(string1[:10]) #slice starting at the beginning of the string up to, but NOT including, index 10
print(string1[:]) #returns the entire string
print(string1[-1]) #returns the last character in the string
print(string1[-2]) #returns the second to last character in the string
print(string1[-9:-1]) #extracts a certain substring using negative indexes
print(string1[-5:]) #returns the last 5 characters in the string
print(string1[:-5]) #returns the string minus its last 5 characters
print(string1[::2]) #adds a third element called step; skips every second character of the string
print(string1[::-1]) #returns string1's elements in reverse order


#slicing using a step
#yeniki 1den 7e kimi 2-2 arta-arta getsin
string2 = "0123456789"

print(string2[1:7:2])