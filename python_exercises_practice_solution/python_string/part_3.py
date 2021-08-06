# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.

def function(str):

    if len(str) < 2:
        print("Empty String")
    else:
        print((str[:2] + str[-2:]))

function("ssasaddffe")

#####solution 2
def string_both_ends(str):
  if len(str) < 2:
    return ''

  return str[0:2] + str[-2:]

print(string_both_ends('w3resource'))
print(string_both_ends('w3'))
print(string_both_ends('w'))
