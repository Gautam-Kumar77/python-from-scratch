#1 program for accepting any value and Decide whether It is Palindrome or Not
v= "12321"
res= "Palindrome: "  if v==v[::-1]  else "Not Palindrome"
print("{} is {}".format(v,res))

st= input("Enter a value: ")
res= "Palindrome" if st==st[::-1] else "Not a Palindrome"
print("{} is {}".format(st, res))

#2 program for accepting any Two Numerical Values and Find Biggest among them and check for Equality
a= float(input("Enter first value: "))
b= float(input("Enter second value: "))

res= a if a>b else b  if b>a else "Both are equal"
# print("{} is greater".format(res))
print("Max({},{})={}".format(a,b,res))

#3 program for accepting any Three Numerical Values and Find Biggest among them and check for Equality
a= float(input("Enter first value: "))
b= float(input("Enter second value: "))
c= float(input("Enter second value: "))

res= a if (a>b) and (a>c) else b if (b>a) and (b>=c) else c if (c>=a) and (c>b) else "All values are queal"
print("Max({} {} {}) = {}".format(a,b,c,res))

#4 program for accepting any Numerical Value and Decide Weather it is +VE or -VE or Zero
n= float (input("Enter a number: "))
res= "Positive" if n>0 else "Negative number" if n<0 else "ZERO"
print("{} is a {} Number".format(n,res))

#5 Write a program to compare two strings and display whether they are equal or not using  if..else operator.
v1= input("Enter first value: ")
v2= input("Enter second value: ")

rsl= "Equal String" if v1==v2 else "Not Equal String"
print("{} and {} = {}".format(v1,v2,rsl))
