# Write a Python program to display the current date and time.

import datetime

now = datetime.datetime.now()

print(" Current date and time : \n")
print(now)  #bunun ile yalniz cari vaxti bu sekilde print edir ve sonun da saniyede qoyur: 2021-07-12 10:53:49.013785 
print(now.strftime("%Y-%m-%d %H:%M:%S"))  #strftime ile ise istediyimiz kimi date-i duze bilirik, misalcun saniyeni yigisdiririq: 2021-07-12 10:53:49