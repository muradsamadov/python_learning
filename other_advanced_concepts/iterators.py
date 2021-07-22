#iterator ile list-deki ededleri bir-bir istifade edir
list = [1,2,3]  #list daxil edirik

i_list = iter(list)  #iter ile listi tanidiriq

print(next(i_list)) #birinci cavab 1
print(next(i_list)) #ikinci cavab 2
print(next(i_list)) #ucuncu cavab 3
print(next(i_list)) #StopIteration; Bele-bele davam edecek

#####
#Generators - special routines that can be used to control the iteration behavior of a loop; defined using the "def" keyword; 
def my_gen(y): #creating a generator function 
    for i in range(10):
        print("i is %d" % i)
        print("y is %d" % y)
        yield i * y   #yields the values one at a time; traversing a sequence up to a certain point, getting the result and suspending the execution

my_object = my_gen(5) #creating a generator object

print(next(my_object)) #manually yield the next element returned by the my_gen() function; raises StopIteration when the sequence is exhausted
print(next(my_object))
print(next(my_object))
print(next(my_object))

