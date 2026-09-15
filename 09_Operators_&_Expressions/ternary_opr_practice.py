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

#program for accepting any Three Numerical Values and Find Biggest among them and check for Equality
a= float(input("Enter first value: "))
b= float(input("Enter second value: "))
c= float(input("Enter second value: "))

res= a if (a>b) and (a>c) else b if (b>a) and (b>=c) else c if (c>=a) and (c>b) else "All values are queal"
print("Max({} {} {}) = {}".format(a,b,c,res))

#program for accepting any Numerical Value and Decide Weather it is +VE or -VE or Zero
n= float (input("Enter a number: "))
res= "Positive" if n>0 else "Negative number"
print("{} is a {} Number".format(n,res))