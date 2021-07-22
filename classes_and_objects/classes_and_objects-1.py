class Myrouter(object):  #class yaradiram ve adini Myrouter qoyuram

    def __init__(self, routername, model, SN, ios):  #__init__ ile yeni funksiya yaradiram ve inputlari daxil edirem. self optionu olmasi mutleqdir
        self.routername = routername  #hemin metodlari daxil edirem
        self.model = model
        self.SN = SN
        self.ios = ios

    def print_router(self):  #yeni print_router adinda funksiya yaradiram. Bu sadece olaraq test ucundur bunu yaratmayada bilerem
        print("The router name is: ",self.routername)
        print("The router model is: ",self.model)
        print("The router SN is: ",self.SN)
        print("The router ios is: ",self.ios)


result = Myrouter("R1","2900","001","002")  #Myrouter class-da olanlari arqument kimi daxil edirem ve result olaraq menimsedirem

result.print_router()  #ve print_router funksiyasini ise saliram

# print(result.print_router)

result2 = Myrouter("R2","2900","001","002")  #arqumentde bezi deyisiklikler edib result2 olaraq menimsedirem

print(result2.routername)  #result2-de olan routername-i pront edir, cavab=R2

result2.routername = "R3"  #gorunduyu kimi routername-i R3 olaraq deyisirem

print(result2.routername)  #ve cavab olaraq R3 qaytarir, belelikle update edirem arqumenti

#getattr, setattr. getattr- ilehal-hazirki arqumenti cavab olaraq qaytarir; setattr-ile ise arqumentde olan deyeri deyisir,update edir

print(getattr(result2, "routername"))  #cavab olaraq R3 qaytarir

setattr(result2, "routername", "R4")  #setattr ile routername-i R4 olaraq update edirik

print(getattr(result2, "routername"))  #cavabda da R4 olaraq print olur

#####
#Classes and objects
class MyRouter(object): #creating a class which inherts from the default "object" class
    def __init__(self, routername, model, serialno, ios): #class constructor; initializing some variables and the method is called whenever you create a new instance of the class 
        self.routername = routername #"self" is a reference to the current instance of the class
        self.model = model
        self.serialno = serialno
        self.ios = ios
 
    def print_router(self, manuf_date):
        print("The router name is: ", self.routername)
        print("The router model is: ", self.model)
        print("The serial number of: ", self.serialno)
        print("The IOS version is: ", self.ios)
        print("The model and date combined: ", self.model + manuf_date)
        
router1 = MyRouter('R1', '2600', '123456', '12.4') #creating an object by simply calling the class name and entering the arguments required by the __init__ method in between parentheses
 
router1.model #accessing the object's attributes; result is '2600'
 
router1.print_router("20150101") #accessing a function (actually called method) from within the class 
The router name is:  R1
The router model is:  2600
The serial number of:  123456
The IOS version is:  12.4
The model and date combined:  260020150101
 
getattr(router2, "ios") #getting the value of an attribute
 
setattr(router2, "ios", "12.1") #setting the value of an attribute
 
hasattr(router2, "ios") #checking if an object attribute exists
 
delattr(router2, "ios") #deleting an attribute
 
isinstance(router2, MyRouter) #verifying if an object is an instance of a particular class
 
class MyNewRouter(MyRouter): #creating a new class (child) inheriting from the MyRouter parent class
    ...
 
issubclass(MyNewRouter, MyRouter) #returns True or False; checking if a class is the child of another class