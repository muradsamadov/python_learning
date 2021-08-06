# Write a Python script to merge two Python dictionaries.


dic1={1:10, 2:20}
dic2={3:30, 4:40}

d = {}

for i in [dic1,dic2]:
    d.update(i)

print(d)