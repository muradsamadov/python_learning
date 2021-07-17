from itertools import *

#chain ile list-leri birlesdiririk
list1 = [1,2,3,'a','b','c']
list2 = [101,102,103,'X','Y']

# chain(list1,list2)

for i in chain(list1,list2):
    print(i)

###chain diger misal###
from itertools import *

list1 = [1,2,3,'a','b','c']
list2 = [101,102,103,'X','Y']

print(list(chain(list1,list2)))  #bu misalda dachain ile list-leri birlesdiririk

###count###
from itertools import *

for i in count(4,15):  #count ile 4den baslayir ustune 15 gele gele gedir: 4+15+15+15...
    if i<100 :
        print(i)
    else:
        break

###cycle###
from itertools import *

list1 = ['Murad', 'Fuad', 'Zahir', 'Nergiz']

for i in cycle(list1):  #cycle ile list1-de olan butun daxil olanlari dovr ederek print edir: 'Murad', 'Fuad', 'Zahir', 'Nergiz','Murad', 'Fuad', 'Zahir', 'Nergiz','Murad', 'Fuad', 'Zahir', 'Nergiz'
    print(i)

###filterfalse###
from itertools import *

list1 = [1,2,3,4,5,6,8,9]

print(list(filterfalse(lambda x: x<=5, list1)))  #filterfalse ile cavab eger TRUE -dursa o FALSE-a cevirib ele print edir. Misal ucun sertde daxil etmisikki 5den biyuk beraber olanlari print ele, o ise eksine edir, cavabda ise 6,7,8 print edir

###islice###
from itertools import *

list1 = [34,33,22,'a','s','d',56,65]

print(list(islice(list1,0,4)))  #islice ile mueyyne bir araligi print edir, bu misalda list1-de 0-4 argumentleri print edir



#####in englist version
#Itertools - built-in Python module for working with iterable data sets
import itertools
 
list1 = [1, 2, 3, 'a', 'b', 'c']
list2 = [101, 102, 103, 'X', 'Y']
 
#chain() - takes several sequences and chains them together
chain(list1, list2)
 
list(chain(list1, list2)) #result is [1, 2, 3, 'a', 'b', 'c', 101, 102, 103, 'X', 'Y']
 
#count() - returns an iterator that generates consecutive integers until you stop it, otherwise it will go on forever
for i in count(10, 2.5):
    if i <= 50:
        print(i)
    else:
        break   #result is printing the numbers between 10 and 50 inclusively, with a step of 2.5
        
#cycle() - returns an iterator that simply repeats the value given as argument infinitely; you have to find a way to break out of the infinite loop
a = range(11, 16)
 
for i in cycle(a):
	print(i) #use Ctrl+C to break out of the infinite loop
    
#filterfalse() - returns the elements for which the function you give as argument returns False
list(filterfalse(lambda x: x < 5, [1, 2, 3, 4, 5, 6, 7])) #in Python 2 the result is [5, 6, 7]; in Python 3 there is no ifilter() like in Python 2, just filter() and filterfalse()
 
#islice() - performs slicing; we can specify a starting point of the slice, an end point and a step
list(islice(range(10), 2, 9, 2)) #result is [2, 4, 6, 8]