# Write a Python program to calculate number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days 

date1 = (2014, 7, 2)
date2 = (2014, 7, 11)

print(int(date2[-1]) - int(date1[-1]))