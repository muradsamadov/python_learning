import re

a = "salam dunya ok 2 1995"

#split ile qeyd olunan simvolu tapir ve onu print etmir ve hemin simvolu tapanda teksti bolur
print(re.split(r"u", a))

#subn ise buradaki misalda bosluqlari tapir ve _ ile evez edir
print(re.subn(r"\s", "_", a))