#map-in menasi funksiyani basqa bir funksiya daxilinde calisdirmaqdir
#map() - takes a function and a sequence as arguments and applies the function to all the elements of the sequence, returning a list as the result
def production(a):  #sade funksiya yaziriq, daxil olan a ededini 10a vursun
    return a*10

r = range(10)  #hemin range-i daxil edirik

print(list(map(production, r)))  #map-in daxilinde hemin funksyani yaziriq ve basqa r deyisenini daxil edirik. Sonra ise list seklinde print edirik

###
r = range(10)

print(list(map((lambda x: x * 5), r)))

###
list1 = range(10)

#filter() - takes a function and a sequence as arguments and extracts all the elements in the list for which the function returns True
print(list(filter(lambda a: a > 5, list1))) #result is [6, 7, 8, 9]
