#gedir operator.txt faylina baxir ve sertlere gore icra edir

import re

def gsm_operator_bul(tel_no):
    patern = r"\d{10}"
    state = re.search(patern , tel_no)
    if state:
        for loop in re.findall(patern , tel_no):
            if loop.startswith("050"):
                return "Azercell operatorudur"
            elif loop.startswith("055"):
                return "Bakcell operatorudur"
            elif loop.startswith("077"):
                return "Nar operatorudur"
            else:
                return "Bele bir operator yoxdur"
    else:
        return "Bele bir pattern yoxdur"

myfile = open("d:\development_codes\python_learning\\regular_expressions\operator.txt", "r")

tel_no = myfile.read()

print(gsm_operator_bul(tel_no))