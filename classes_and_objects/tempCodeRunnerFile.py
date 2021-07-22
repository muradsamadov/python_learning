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

result2 = Myrouter("R2","2900","001","002")

print(result2.routername)