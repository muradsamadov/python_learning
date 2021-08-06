# Write a Python program to convert Python dictionary object (sort by key) to JSON data. Print the object members with indent level 4.

import json
j_str = {'4': 5, '6': 7, '1': 3, '2': 4}
print("Original String:")
print(j_str)
print("\nJSON data:")
print(json.dumps(j_str, sort_keys=True, indent=4))  # burada sort_keys ile reqemleri ardicil olaraq duzuruk, indent ile ise yuxaridan asagiya siralayiriq 4-e kimi ve soldan saga 4 setir qoyuruq
