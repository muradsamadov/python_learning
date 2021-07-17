import re

#hemin some.txt faylinin path-ni gosteririk
myfile = open("d:\development_codes\python_learning\\regular_expressions\some.txt", "r")

#pattern-e hemin sozu tanidiriq ve burada \d yalniz reqemleri ifade edir yeniki misal ucun bu bele ola biler: Unix1111, Unix2222 ve s. ne qeder \d yaziriqsa bir o qdr simvolda reqem edir
pattern = "Unix\d\d\d\d"

#re.search olaraq qeyd edirikki myfile-da pattern-e ne tanitmisiqsa onu search edir ve cavab olaraq tapirki Unix1696 var
state = re.search(pattern , myfile.read())

#neticeni print edirik: Unix1696
print(state.group())


###
import re

#hemin some.txt faylinin path-ni gosteririk
myfile = open("d:\development_codes\python_learning\\regular_expressions\some.txt", "r")

#pattern-e hemin sozu tanidiriq ve burada \s bosluqlari ifade edir yeniki misal ucun bu bele ola biler: 1969 1234 ve s. 
pattern = "\d\d\d\d\s\d\d\d\d"
#qeyd edimki her defe bu qeder simvolu yeniki \d \s leri yazmaq uzun olur buna gorede bele yazmaqda olar:
pattern = "\d{3,4}\s\d{2,}" #burada \d{3,4} - 3 yadaki 4 dene reqem ola biler, \d{4} yalniz 4 eded olmalidir, ondan asagi yadaki yuxari misalcun \d{3} olsa ve reqem 4 reqemlidirse onun yalniz ilk 3 reqemini print edir. \d{2,} - en azi iki dene olmalidir
pattern = "\d+" #\d+ 1den artiq reqem demekdir
pattern = "\w*\d+"

#re.search olaraq qeyd edirikki myfile-da pattern-e ne tanitmisiqsa onu search edir ve cavab olaraq tapirki 1969 1995 var
state = re.search(pattern , myfile.read())

#neticeni print edirik: 1969 1995
print(state.group())

###
import re

#hemin some.txt faylinin path-ni gosteririk
myfile = open("d:\development_codes\python_learning\\regular_expressions\some.txt", "r")

#\w hem herf hemdeki reqemler daxildir. \w{7,} ise azi 7 olmaqla
pattern = "\w{7,}"

for state in re.findall(pattern , myfile.read()):
    print(state)
