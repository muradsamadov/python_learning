# *args ile daha qisa funksiya yazmaq olur. Asagidaki misallara baxaq

def power(*args):
    result = 1
    for arg in args:
        result = result * arg
    return result

print(power(2,3))

#####
def ededi_orta(*args):
    return sum(args) / len(args)

print(ededi_orta(2,3,4,5))

# *kwargs ise key ve value olaraq daxil etmek olur. Asagidaki misala baxaq

def function(**kwargs):
    for kwarg in kwargs:
        print(kwarg)

print(function(name = "Murad", surname = "Samadov"))

#####
def function(**kwargs):
    print(kwargs)

print(function(name = "Murad", surname = "Samadov"))