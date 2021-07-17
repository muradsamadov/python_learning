#Files - opening and reading a file in the same directory/folder
myfile = open("D:\\development_codes\\python_learning\\file_operations\\routers.txt", "r") #"r" is the file access mode for reading and it is the default mode when opening a file

#myfile hansi access modda oldugunu print edir, yeniki read moddadir
print(myfile.mode) #checking the mode in which a file has been opened
 
#myfile-da olanlari print edir, yeniki faylda ne varsa cat edir 
print(myfile.read()) #method that returns the entire content of a file in the form of a string

#myfile faylinda olan ilk 5 bayti cat edir.Qeyd:Eger bu printden evvel  myfile.read() -i icra etmisikse bu hisse bow sekilde print olacaq.Sebeb ise bunun bas hisseden fayli oxumamagidir. Bunun helli seek ile mumkundur ve asagida qeyd olunub
print(myfile.read(5)) #returning only the first 5 characters (bytes) in the file

#seek ile hemin faylin lap evvelki setrine qayidir ve cat edir. Daha sonra ise myfile.read(5) edirik 
myfile.seek(0) #moving the cursor at the beginning of the file
 
myfile.tell() #checking the current position of the cursor inside the file

#yalnizca birinci setiri cat edir
print(myfile.readline()) #returns the file content one line a ta time, each time you use the method

#buntun setirleri bir setir altinda cat edir
print(myfile.readlines()) #returns a list where each element is a line in the file

