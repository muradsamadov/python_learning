x = "Cisco"
y = "Switch"

#x ve y stringlerini birlesdirir
print(x+y)

#x stringini 3 defe yanbayan print edir
print(x*3)

#eger a xarakteri x stringinde varsa TRUE qaytarir, eks halda FALSE
print("a" in x)

#gorunduyu kimi ardicil olaraq %s=2600XM %d=2 %f=12.4 olaraq print edir
print("Cisco model: %s, %d WAN slots, IOS %f" % ("2600XM", 2, 12.4))

#burada %.1f=12.4 olaraq print edir, yenik vergulde nece eded print etsin
print("Cisco model: %s, %d WAN slots, IOS %.1f" % ("2600XM", 2, 12.4))

#burada da yuxaridaki kimi eyni neticeni verir, sadece olaraq format operatorundan istifade edir
print("Cisco model: {}, {} WAN slots, IOS {}".format("2600XM", 2, 12.4))

#burada ise ardicil olaraq yox, ozun stringleri ozune gore print edirsen
print("Cisco model: {2}, {0} WAN slots, IOS {1}".format("2600XM", 2, 12.4))

