#write modu ile yeni fayl yaradiriq eger fayl yoxdursa
#Files - writing and appending to a file
newfile = open("D:\\development_codes\\python_learning\\file_operations\\newfile.txt", "w") #opens/creates a new file for writing; the "w" method also creates the file for writing if the file doesn’t exist and overrides the file if the file already exists; remember to close the file after writing to it to save the changes!
 
newfile.writelines(["Cisco", "Juniper", "HP", "\n"]) #this method takes a sequence of strings as an argument and writes those strings to the file

#append modu ile cari faylin uzerinde write edir 
newfile = open("D:\\development_codes\\python_learning\\file_operations\\newfile.txt", "a") #opening a file for appending

newfile.writelines(["\n", "Cisco_append", "Juniper_append", "HP_append", "\n"])
 
newfile = open("D:\\development_codes\\python_learning\\file_operations\\newfile.txt", "w+") #opens a file for both writing and reading at the same time
 
newfile.writelines(["\n", "Cisco_2", "Juniper_2", "HP_2", "\n"])

newfile = open("newfile.txt", "x") #opens for exclusive creation, failing if the file already exists
 
#Files - closing a file
newfile.closed #checking if a file is closed
 
newfile.close() #closing a file
 
with open("python.txt", "w") as f: #using the with-as solution, the files gets closed automatically, without needing the close() method
    f.write("Hello Python!\n")