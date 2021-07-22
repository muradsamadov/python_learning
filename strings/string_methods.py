#Strings - indexing
#daxil edilen indexin necenci xarakter olmasini print edir
a = "Cisco Switch"

print(a.index("i"))

#Strings - character count
#hemin string-de nece dene simvol oldugunu print edir
a = "Cisco Switch"

print(a.count("i"))

#Strings - finding a character
#daxil edilen stringi find edir ve necenci xarakter olmasini gosterir
a = "Cisco Switch"

print(a.find("w"))
print(a.find("tch"))

#Strings - converting the case lowercase and uppercase
a = "Cisco Switch"

print(a.lower())
print(a.upper())

#Strings - checking whether the string starts and ends with a character
#stringin ilk ve sonuncu herflerini xarakter olaraq daxil edilir, xarakterde boyuk-kicik herfler nezere alinir
a = "Cisco Switch"

print(a.startswith("C"))
print(a.endswith("h"))

#remove whitespaces
# bos olan setrleri silir
a = "   Cisco Switch"

print(a.strip())

#remove a certain character
#butun $ simvollarini silib print edir
a = "$$Cisco Switch$$$"

print(a.strip("$"))

#replace each space character with the absence of any character
#butun $ simvollarini silir ve yerine bosluq olmayan-i yazir
a = "$$Cisco Switch$$$"

print(a.replace("$",""))

#Strings - splitting a string by specifying a delimiter; the result is a list
#butun vergulleri silir
d = "Cisco,Juniper,HP,Avaya,Nortel"

print(d.split(","))

#Strings - inserting a character in between every two characters of the string / joining the characters by using a delimiter
#butun xarakterler arasi _ isaresi ile print edir
a = "Cisco Switch"

print("_".join(a))
