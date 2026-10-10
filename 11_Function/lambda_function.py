#Ex.1 Define Anonymous Function for Adding Two Numbers
addop= lambda a,b : a+b

a= float(input('Enter first number: '))
b= float(input("Enter second number: "))
res= addop(a,b)
print(res)

#Ex2. Define Anonymous Function for Checking Palindrome
palindrome =  lambda val: "Palindrome" if val==val[::-1] else "Not Palindrome"
value= input("Enter a string: ")
res= palindrome(value)
print("{} is {}".format(value, res))

#Ex3. Program for accepting Two Values and find Biggest among them and check for Equality
num= lambda a,b: a if a>b  else b if b>a else "Both values are equal"
a= float(input("Enter First Number: "))
b= float(input("Enter Second number: "))
res= num(a,b)
print("Max({},{})= {}".format(a,b,res))