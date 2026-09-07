#Single line assignment
a=10
b=20
c= a+b
print(c)

#Multi line assignment
a= float(input("Enter first Number: "))
b= float(input("Enter Second Number: "))

ap, sp,mp,dp,fd,md,ep = a+b, a-b, a*b, a/b, a//b, a%b, a**b
print("Sum: {} + {} = {} ".format(a,b,ap))
print("Subtraction: {} - {} = {}".format(a,b,sp))
print("Multiplication: {} * {} = {}".format(a,b,mp))
print("Division: {} / {} = {}".format(a,b,dp))
print("Floor Division: {} // {} = {}".format(a,b,fd))
print("Remainder: {} % {} = {}".format(a,b,md))
print("Exponential: {} ** {} = {}".format(a,b,ep))