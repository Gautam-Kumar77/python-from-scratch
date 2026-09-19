#Ex 1. Write a Python program to check whether a person has a movie ticket using a simple if statement.
# If the ticket is available, display messages for entering the theater, watching the movie, and understanding the message.

tkt= input("Do you have a ticket(yes/no)?")
if tkt.lower()=="yes":
    print("\tWelcome to Theatre")
    print("\tEnjoy Movie!")
print("Go to Home")

#Ex2. program for accepting any value and Decide whether It is Palindrome or not
val= input("Enter any Value: ")
if val==val[::-1]:
    print("{} is Palindrome".format(val))
if val!=val[::-1]:
    print("{} is not Palindrome".format(val))
print("Program executed successfully")

# Ex3. Program for accepting any Numerical value and Decide whether It is +VE or -VE or Zero
num= int(input("Enter any Numerical value: "))
if num>0:
    print("{} is +ve number".format(num))
if num<0:
    print("{} is -ve number".format(num))
if num==0:
    print("{} is Zero")

# Ex4. Program for accepting any +VE Numerical Integer Value and decide whether It is Even OR Odd
num= int(input("Enter a number"))
if num<0:
    print("Please Enter Positive number")
if num>0 and num%2==0:
    print("Number is Positive and {} is Even Number.".format(num))
if num>0 and num%2!=0:
    print("Number is Positive but {} is Odd Number.".format(num))

# Ex5. Write a Python program to calculate Simple Interest using P, T, and R. Validate that all three values are greater than zero using simple if statements and display appropriate error messages for invalid values.
p= float(input("Enter Principle: "))
r= float(input("Enter rate: "))
t= float(input("Enter time: "))
si = (p*r*t)/100
if p>0 and r>0 and t>0:
    print("Principle:", p)
    print("Rate:", r)
    print("Time:", t)
    print("Simple Interest:", si)

if p<=0:
    print("Invalid Principle")
if t<=0:
    print("Invalid time")
if r<=0:
    print("Invalid rate")
print("Program Execution Completed")

#Ex6. Program for accepting and display Its Name
num= int(input("Enter a number: "))
if num==0:
    print("{} is Zero".format(num))
if num==1:
    print("{} is One".format(num))
if num==2:
    print("{} is Two".format(num))
if num==3:
    print("{} is Three".format(num))
if num==4:
    print("{} is Four".format(num))
if num==5:
    print("{} is Five".format(num))
if num==6:
    print("{} is Six".format(num))
if num==7:
    print("{} is Seven".format(num))
if num==8:
    print("{} is Eight".format(num))
if num==5:
    print("{} is Nine".format(num))
if num>9:
    print("It is Positive number")
if num in range(-1,-10,-1):
    print("It is Negative Digit")
if num<0 and num not in range(-1,-10,-1):
    print("It is negative number")

