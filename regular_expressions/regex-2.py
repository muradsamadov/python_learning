import re

a = "I enjoy learning Python 3"

#a-da olan yalniz kicik herfleri print edir
result = re.findall(r"[a-z]", a)

#a-da olan yalniz boyuk herfleri print edir
result2 = re.findall(r"[A-Z]", a)

#a-da olan yalniz abn herflerini print edir
result3 = re.findall(r"[abn]", a)

#a-da a olmayan butun ne varsa print edir
result4 = re.findall(r"[^a]", a)

print(result,result2,result3,result4)