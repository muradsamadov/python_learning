import my_module  #hemin direktoriyada yerlesen my_module.py faylini import edir. Bu halda ise my_module.py faylinda olan kodlar burada aid olur

print("This is my app")

print(my_module.my_var)  #belelikle my_module.py faylinda olan my_var-i print edirik

my_module.my_function()  #elecede my_module.py faylinda olan my.function funksiyasini cagiririq

###

from my_module import *  #burada ise kod hissesinde daha seliqeli yazilmasi ucun my_module funksiyasindan istifade edilmir. from ile my_module.py faylinda olanlari bu fayla import edir

print("This is my app")

print(my_var)  #belelikle my_module.py faylinda olan my_var-i print edirik

my_function()  #elecede my_module.py faylinda olan my.function funksiyasini cagiririq

