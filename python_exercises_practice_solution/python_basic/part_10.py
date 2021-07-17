# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# Sample value of n is 5
# Expected Result : 615

number = int(input("Please input number: "))

x1 = int("%i" % number)
x2 = int("%i%i" % (number,number))  #qeyd etmeliyem ki, ne qdr argument qeyd edirikse bir o qederde number olan variableni qeyd etmeliyik, asagidaki kimi hemde
x3 = int("%i%i%i" % (number,number,number))

print(x1 + x2 + x3)