#Ex 1. Write a Python program to check whether a person has a movie ticket using a simple if statement.
# If the ticket is available, display messages for entering the theater, watching the movie, and understanding the message.

# tkt= input("Do you have a ticket(yes/no)?")
# if tkt.lower()=="yes":
#     print("\tWelcome to Theatre")
#     print("\tEnjoy Movie!")
# print("Go to Home")
#
# #Ex2. program for accepting any value and Decide whether It is Palindrome or not
# val= input("Enter any Value: ")
# if val==val[::-1]:
#     print("{} is Palindrome".format(val))
# if val!=val[::-1]:
#     print("{} is not Palindrome".format(val))
# print("Program executed successfully")
#
# # Ex3. Program for accepting any Numerical value and Decide whether It is +VE or -VE or Zero
# num= int(input("Enter any Numerical value: "))
# if num>0:
#     print("{} is +ve number".format(num))
# if num<0:
#     print("{} is -ve number".format(num))
# if num==0:
#     print("{} is Zero")
#
# # Ex4. Program for accepting any +VE Numerical Integer Value and decide whether It is Even OR Odd
# num= int(input("Enter a number"))
# if num<0:
#     print("Please Enter Positive number")
# if num>0 and num%2==0:
#     print("Number is Positive and {} is Even Number.".format(num))
# if num>0 and num%2!=0:
#     print("Number is Positive but {} is Odd Number.".format(num))
#
# # Ex5. Write a Python program to calculate Simple Interest using P, T, and R. Validate that all three values are greater than zero using simple if statements and display appropriate error messages for invalid values.
# p= float(input("Enter Principle: "))
# r= float(input("Enter rate: "))
# t= float(input("Enter time: "))
# si = (p*r*t)/100
# if p>0 and r>0 and t>0:
#     print("Principle:", p)
#     print("Rate:", r)
#     print("Time:", t)
#     print("Simple Interest:", si)
#
# if p<=0:
#     print("Invalid Principle")
# if t<=0:
#     print("Invalid time")
# if r<=0:
#     print("Invalid rate")
# print("Program Execution Completed")
#
# #Ex6. Program for accepting and display Its Name
# num= int(input("Enter a number: "))
# if num==0:
#     print("{} is Zero".format(num))
# if num==1:
#     print("{} is One".format(num))
# if num==2:
#     print("{} is Two".format(num))
# if num==3:
#     print("{} is Three".format(num))
# if num==4:
#     print("{} is Four".format(num))
# if num==5:
#     print("{} is Five".format(num))
# if num==6:
#     print("{} is Six".format(num))
# if num==7:
#     print("{} is Seven".format(num))
# if num==8:
#     print("{} is Eight".format(num))
# if num==5:
#     print("{} is Nine".format(num))
# if num>9:
#     print("It is Positive number")
# if num in range(-1,-10,-1):
#     print("It is Negative Digit")
# if num<0 and num not in range(-1,-10,-1):
#     print("It is negative number")


# Accept a number and print "Divisible by both 3 and 5" if it is divisible by both.
# n= int(input("Enter a number"))
# if n%3==0 and n%5==0:
#     print("It is divisible by 3 and 5")
# print("Program Terminated")
#
# # Accept two numbers and print "First number is greater" if the first number is greater than the second.
# n= int(input("Enter a number: "))
# n1= int(input("Enter a number: "))
# if n>n1:
#     print("{} is greater".format(n))
#
# # Accept a temperature and print "High Temperature" if the temperature is greater than 40°C.
# temp= int(input("Enter Temperature: "))
# if temp>40:
#     print("High Temperarure")
#
# # Accept marks and print "Qualified" if marks are 40 or above.
# marks= int(input("Enter a number"))
# if marks>40:
#     print("Qualified")
#
# # Accept a salary and print "High Salary" if the salary is greater than 50,000.
# sal= int(input("Enter a number: "))
# if sal>50000:
#     print("High Salary")


# # Accept a number and print "Number is within range" if it is between 10 and 50, inclusive.
# num= int(input("Enter number 10 and 50"))
# num1= range(10,51,1)
# if num in num1:
#     print("Number is within range")
#
# Accept an integer and print "Three Digit Number" if the number is between 100 and 999.
num= int(input("Enter number from 100 to 999"))
num1= range(100,1000,1)
if num in num1:
    print("Three Digit Number.")
# Uppercase Character
# Accept a character and print "Uppercase Alphabet" if it is between A and Z.
# Lowercase Character
# Accept a character and print "Lowercase Alphabet" if it is between a and z.
# Divisible by 2 and 3
# Accept a number and print "Divisible by 2 and 3" if it is divisible by both.
