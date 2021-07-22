def my_first_function(x,y,z):
    sum_xyz = (x + y) * z
    return sum_xyz

print(my_first_function(1,2,3))

print(my_first_function(x = 1,y = 2,z = 3))

###

def function1(x, *args): #specifying a variable number of positional parameters in a function definition; args is a tuple
    print(x)

function1("hello")

###

def function1(x, *args):
    print(x)
    print(args)

function1("hello", 1,2,3)

###

def function1(x, *args):
    print(x)
    for argument in args:
        print(argument)

print(function1("hello", 1,2,3))