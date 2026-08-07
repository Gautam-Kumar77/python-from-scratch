a= True
print(a, type(a))
b= False
print(b, type(b))

num1= True
num2= False
sum= num1+num2
sum1= num2-num1
print(sum, type(sum))
print(sum1, type(sum1))

print(True*2-False)
print(2-False*True+2)
print(True/True)
print(False/True)
print(True/False)  #ZeroDivisionError: division by zero
print(False/False)   #ZeroDivisionError: division by zero
print(0x46c1*True+5-False)
print(0b1011*False-True)

c= true
print(c, type(c)) #NameError: name 'true' is not defined
d= false
print(d, type(d)) #NameError: name 'false' is not defined