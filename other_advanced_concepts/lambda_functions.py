#lambda funksiyalar return-u daha tez qaytarmaq ucun ist. olunur.Yeniki sen bir funksiya yaza bilersen ammaki onu daha qisa sekilde labmda funks. ilede yazmaz olur:
def power(x):
    return x*x

result = power

print(result(2))  #power funksiyasi ile 

a = lambda x: x*x #bu ise lambda ile daha sade yeni ki, power funk-in dahada qisaldilmisi oldu ve daha rahat oldu lambda ile etmek

print(a(2))

a = lambda x,y: x*y  #lambda funk. ile x ve y-i daxil edirik

print(a(2,4))