# # Ex:1 Write a program to find the greater of two numbers using the if..else operator.
# a= float(input("Enter First Number: "))
# b= float(input("Enter Second Number: "))
# res= a if a>b else b if b>a else "Both values are equal."
# print("Max({}, {})={}".format(a,b,res))
#
# #Ex:2 Write a program to find the smaller of two numbers using the if..else operator.
# a= float(input("Enter First Number: "))
# b= float(input("Enter Second Number: "))
# res= a if a<b else b if b<a else "Both values are equal"
# print("Min({}, {})={}".format(a,b,res))
#
# #Ex:3 Write a program to check whether a number is even or odd using the if..else operator.
# a= float(input("Enter a Number to check whether it is odd or even: "))
# res1= "Even" if a%2==0 else "Odd"
# print("{} is an {} Number".format(a,res1))
#
# #Ex:4 Write a program to check whether a number is positive or negative using the if..else operator.
# a= float(input("Enter a Number: "))
# res= "+ve" if a>0 else "-ve"
# print("{} is a {} number.".format(a,res))
#
# #Ex:5 Write a program to check whether a number is positive, negative, or zero using nested if..else operators.
# a= float(input("Enter a Number: "))
# res= "+ve" if a>0 else "-ve" if a<0 else "ZERO"
# print(res)
#
# #Ex:6 Write a program to check whether a person is eligible to vote based on age using the if..else operator.
# age= int(input("Enter Your Age: "))
# res= "You are eligible to give vote" if (age>=18) and (age<=120) else "You are not eligible to give vote" if age<121 else "You are above 120 You must die now"
# print(res)
from idlelib.rpc import response_queue

#Ex:7 Write a program to determine whether a student has passed or failed based on marks using the if..else operator.
# marks= float(input("Enter Your Makrs: "))
# res= "You are Passed" if (marks>=90) and (marks <=100) else "You are Failed"
# print(res)
#
# #Ex:8 Write a program to calculate the grade of a student (A, B, C, or F) using nested if..else operators.
# marks= float(input("Enter Your Makrs: "))
# res= "Grade:A" if (marks>=90) and (marks <=100) else "Grade:B" if (marks<=89) and (marks>=70) else "Grade C" if marks<=69 and marks>=60 else "Grade F"
# print(res)

#Ex:9 Write a program to find the largest of three numbers using nested if..else operators.
# a= float(input("Enter a number: "))
# b= float(input("Enter a number: "))
# c= float(input("Enter a number: "))
# res= a if a>b and a>c else b if b>a and b>c else c
# print("{} {} {} = {} is greatest number".format(a,b,c,res))

#Ex:10 Write a program to find the absolute value of a number using the if..else operator.
# n= float(input("Enter a number: "))
# res= n if n>0 else n*-1
# print(res)
#
# #Ex:11 Write a program to find the absolute difference between two numbers using the if..else operator.
# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
#
# res = a - b if a > b else b - a
# print("Absolute difference =", res)
# print(res)

#Ex:12 Write a program to check whether a given year is a leap year using the if..else operator.
# year= int(input("Enter year"))
# res= "Leap Year" if year%400==0 or year%4==0 and  not(year%100==0) else "Not Leap Year"
# print(res)

#Ex:13 Write a program to check whether a character is a vowel or a consonant using the if..elspecifically for se operator.
# ltr= input("Enter a character: ")
# res= "Vowel" if ltr.lower() in 'aeiou' else "Consonant"
# print(res)

#Ex:14 Write a program to check whether a given character is an alphabet or not using the if..else operator.
# alp= input("Enter a character")
# res= "It is Alphabet" if ("a" <= alp <= "z") or ("A" <= alp <= "Z") else "It is Not Alphabet"
# print(res)

#Ex:15 Write a program to check whether a character is uppercase or lowercase using the if..else operator.
# alp= input("Enter a character: ")
# res= "It is uppercase" if alp >= "A" and alp <="Z" else  "It is lowercase" if alp >= "a" and alp <="z" else "Invalid Input"
# print(res)
#
# #Ex:16 Write a program to check whether a number is divisible by 5 using the if..else operator.
# n= int(input("Enter a number: "))
# res= "Divisible by 5" if n%5==0 else "Not Divisible by 5"
# print("{} is {}".format(n, res))

#Ex17: Write a program to check whether a number is divisible by both 3 and 5 using the if..else operator.
# num= int(input("Enter a number:- "))
# res= "Divisible by 3 and 5" if num%3==0 and num%5==0 else "not divisible by 3 and 5"
# print("{} is {}".format(num,res))

#Ex18: Write a program to determine whether a number is a single-digit number or a multi-digit number using the if..else operator.
# num= int(input("Enter a number:- "))
# res= "Single Digit Number" if (num<=9) and (num>=-9) else "Multi Digit Number"
# print("{} is {} ".format(num,res))

#Ex19: Write a program to determine whether a person is eligible for a senior citizen discount using the if..else operator.
# age= int(input("Enter Age:- "))
# res= "Eligible" if age>60 else "not eligible"
# print("{} is {}".format(age,res))

# #Ex20: Write a program to determine whether a person is eligible for a driving license based on age using the if..else operator.
# age= int(input("Enter your age: "))
# res= "eligible for driving license" if age>=18 else "Not eligible for driving license"
# print("Your age is {} so you are {}".format(age, res))
#
# #Ex:21 Write a program to determine whether a temperature indicates a hot day or a cool day using the if..else operator.
# temp= int(input("Enter Temperature: "))
# res= "Hot day" if temp>=30 else "cool day"
# print("Temperature is {} so it is {}".format(temp, res))

# #Ex22: Write a program to determine whether a business transaction results in profit or loss using the if..else operator.
# cost= int(input("Enter Cost Price: "))
# selling= int(input("Enter Selling Price: "))
# res= "Profit" if selling>cost else "Loss" if cost>selling else "No profit and no loss"
# print(res)
#
# #Ex23: Write a program to find the maximum among two entered numbers using the if..else operator.
# num1= int(input("Enter first number: "))
# num2= int(input("Enter second number: "))
# res = num1 if num1>num2 else num2
# print(res)

# #Ex24: Write a program to find the minimum among two entered numbers using the if..else operator.
# num1= int(input("Enter first number: "))
# num2= int(input("Enter second number: "))
# res = num1 if num1<num2 else num2
# print(res)

# #Ex25: Write a program to check whether a given number is a multiple of 10 using the if..else operator.
# num= int(input("Enter a number: "))
# res= "Multiply of 10" if num%10==0 else "Not Multiply of 10"
# print("{} is {}".format(num, res))
#
# #Ex26: Write a program to check whether a given number is greater than 100 using the if..else operator.
# num1= int(input("Enter a number: "))
# res= "Greater than 100" if num1>100 else "Not greater than 100"
# print("{} is {}".format(num1, res))


# Write a program to determine whether an entered salary qualifies for income tax based on a specified threshold using the if..else operator.
amt= float(input("Enter a amount: "))
res= "You have to pay taxes" if amt>120000 else "You dont have to pay taxes"
print("{} is So {}".format(amt,res))

# Write a program to determine whether a person can enter a movie theater based on the age restriction using the if..else operator.

# Write a program to determine whether a student is eligible for a scholarship based on marks using the if..else operator.
# Write a program to compare two strings and display whether they are equal or not using the if..else operator.