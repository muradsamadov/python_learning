#Task bundan ibaretdir ki, some.txt daxilinde Linux sozunu axtaririq ve olub-olmamasini check edirik

import re

#hemin some.txt faylinin path-ni gosteririk
myfile = open("d:\development_codes\python_learning\\regular_expressions\some.txt", "r")

#pattern olan hissede reqem, herf ne oldu yaza bilersen ve hemin sozuaxtarista istifade edecik
#burada boyuk ve kicik simvollar arasinda ferq var, bu numunede linux yox Linux sozunu tanidiram
pattern = "Linux"

#bu komanda ile ise hemin fayli umumi olaraq cat edirik, hal-hazirda ehtiyac olmadigi ucun kommente aliriq
# print(myfile.read())

#re.search ile ise import olaraq teyin etdiyim re-ye muraciet edir ve gedir myfile-da patter olaraq ne teyin etmisikse yeni "Linux" sozunu bura teyin etmisik
#yeniki pattern "Linux" sozu myfile-da varsa
state = re.search(pattern , myfile.read())

#group ile pattern neye beraberdirse eger hemin soz varsa onu cat edir
print(state.group())