#Functions - Basics
def my_first_function():  #funksiya yaradiriq ve adini my_first_function qoyuruq.
    print("Hello Python")

my_first_function()  #yuxarida qeyd olunan my_first_function funksuyasini ise burda istifade edirik.

###

def my_first_function(x):
    print(x)

my_first_function("Hello")

###

def my_second_function(x,y):
    print("Hello " + x)
    print("Hello " + y)

my_second_function("Python","Java")

###

def my_sum(x, y): #defining a function that takes two parameters
    sum = x + y
    return sum #this statement is used to exit a function and return something when the function is called
 
print(my_sum(5,6))