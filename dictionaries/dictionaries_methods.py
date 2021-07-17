dict1 = {"Vendor": "Cisco", "Model": "2600", "IOS": "12.4", "Ports": "4"}
 
print(dict1)

#returns "Cisco"; extracting a value for a specified key
print(dict1["Vendor"]) #Vendor-key, Cisco-value dir. Vendor key-ne olani print ele

#adds a new key-value pair to the dictionary
dict1["RAM"] = "128" #Yeni RAM=128 key=value artiririq

print(dict1)

#modifies an existing key-value pair
dict1["IOS"] = "12.3" #IOS key-ne aid olan value-ni 12.3 olaraq deyisdiririk

print(dict1)

#deleting a key-value pair from the dictionary
del dict1["Ports"] #Ports key-ni silirik

print(dict1)

#returns the number of key-value pairs in the dictionary
print(len(dict1)) #uzunlugu print edirik, cavab 4 olaraq qayidir

#verifies if "IOS" is a key in the dictionary
print("IOS" in dict1) #True qaytarir

#verifies if "IOS2" is not a key in the dictionary
print("IOS2" in dict1) #False qaytarir

#returns a list having the values in the dictionary as elements
print(dict1.values()) #butun value-ri print edir

#returns a list having the keys in the dictionary as elements
print(dict1.keys()) #butun key-ri print edir

print(list(dict1.keys())) #bu formadada key-leri print etmek olur

#returns a list of tuples, each tuple containing the key and value of each dictionary pair
print(dict1.items()) #bu halda key-value ayrilmis sekilde print edir