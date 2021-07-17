#Task bundan ibaretdir ki, some.txt daxilinde Linux olan butun sozleri for loop u ile axtaririq ve olub-olmamasini check edirik

import re

#hemin some.txt faylinin path-ni gosteririk
myfile = open("d:\development_codes\python_learning\\regular_expressions\some.txt", "r")

#pattern olan hissede reqem, herf ne oldu yaza bilersen ve hemin sozuaxtarista istifade edecik
#burada boyuk ve kicik simvollar arasinda ferq var, bu numunede linux yox Linux sozunu tanidiram
pattern = "Linux"

#butun pattern-e bereber olan sozleri tapmaq ucun ise re.findall -dan istifade edirik
for soz in re.findall(pattern , myfile.read()):
    print(soz)
