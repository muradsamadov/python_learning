# Write a Python program to accept a filename from the user and print the extension of that.
# Sample filename : abc.java
# Output : java

filename = input("Please input filename: ")

file = filename.split(".")

print(repr(file[-1]))  #repr ile cavabi '' -bu dirnaq icinde yazirsan