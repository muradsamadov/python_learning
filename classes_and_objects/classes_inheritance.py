class Myrouter():  #class yaradiram ve adini Myrouter qoyuram

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

class Mynewrouter(Myrouter):  #burada qeyd olunan hissede yeni Mynewrouter adinda class yaradilib ve join olub Myrouter class-na.Buna Inheritance deyilir yeni ki getsin Myrouter class-dakilarada join olub istifade ede bilsin

    def __init__(self, routername, model, SN, ios, portno):  #yeni portno inputu daxil edirem
        Myrouter.__init__ (self, routername, model, SN, ios)  #Myrouter class-da olanlari daxil edirem
        self.portno = portno  #portno self olaraq tanidiram

    def print_new_router(self, string):  #yeniden yeni funksiya yarada bilerem
        print(string + self.model)  #yaradilan funksiyada Myrouter class-da olan model inputundan istifade edirem

new_router1 = Mynewrouter("R5","3000","003","004","10")

print(new_router1.model)