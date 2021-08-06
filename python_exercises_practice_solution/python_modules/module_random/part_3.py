#  Write a Python program to generate a random alphabetical character, alphabetical string and alphabetical string of a fixed length. Use random.choice()

import random, string

max_length = 255
s = ""

for i in range(random.randint(1, max_length)):
    s+= random.choice(string.ascii_letters)

print(s)

print(string.ascii_letters)
print(random.choice(string.ascii_letters))