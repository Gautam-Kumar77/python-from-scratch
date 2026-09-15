# Ex:1 Write a program to find the greater of two numbers using the if..else operator.
a= float(input("Enter First Number: "))
b= float(input("Enter Second Number: "))
res= a if a>b else b if b>a else "Both values are equal."
print("Max({}, {})={}".format(a,b,res))

#Ex:2 Write a program to find the smaller of two numbers using the if..else operator.
a= float(input("Enter First Number: "))
b= float(input("Enter Second Number: "))
res= a if a<b else b if b<a else "Both values are equal"
print("Min({}, {})={}".format(a,b,res))

#Ex:3 Write a program to check whether a number is even or odd using the if..else operator.
a= float(input("Enter a Number to check whether it is odd or even: "))
res1= "Even" if a%2==0 else "Odd"
print("{} is an {} Number".format(a,res1))

#Ex:4 Write a program to check whether a number is positive or negative using the if..else operator.
a= float(input("Enter a Number: "))
res= "+ve" if a>0 else "-ve"
print("{} is a {} number.".format(a,res))

Write a program to check whether a number is positive, negative, or zero using nested if..else operators.
a= float(input("Enter a Number: "))
res= "+ve" if a>0 else "-ve" if a<0 else "ZERO"
print(res)

# Write a program to check whether a person is eligible to vote based on age using the if..else operator.
age= int(input("Enter Your Age: "))
res= "You are eligible to give vote" if (age>=18) and (age<=120) else "You are not eligible to give vote" if age<121 else "You are above 120 You must die now"
print(res)
# Write a program to determine whether a student has passed or failed based on marks using the if..else operator.
# Write a program to calculate the grade of a student (A, B, C, or F) using nested if..else operators.
# Write a program to find the largest of three numbers using nested if..else operators.
# Write a program to find the absolute value of a number using the if..else operator.
# Write a program to find the absolute difference between two numbers using the if..else operator.
# Write a program to check whether a given year is a leap year using the if..else operator.
# Write a program to check whether a character is a vowel or a consonant using the if..else operator.
# Write a program to check whether a given character is an alphabet or not using the if..else operator.
# Write a program to check whether a character is uppercase or lowercase using the if..else operator.
# Write a program to check whether a number is divisible by 5 using the if..else operator.
# Write a program to check whether a number is divisible by both 3 and 5 using the if..else operator.
# Write a program to determine whether a number is a single-digit number or a multi-digit number using the if..else operator.
# Write a program to determine whether a person is eligible for a senior citizen discount using the if..else operator.
# Write a program to determine whether a person is eligible for a driving license based on age using the if..else operator.
# Write a program to determine whether a temperature indicates a hot day or a cool day using the if..else operator.
# Write a program to determine whether a business transaction results in profit or loss using the if..else operator.
# Write a program to find the maximum among two entered numbers using the if..else operator.
# Write a program to find the minimum among two entered numbers using the if..else operator.
# Write a program to check whether a given number is a multiple of 10 using the if..else operator.
# Write a program to check whether a given number is greater than 100 using the if..else operator.
# Write a program to determine whether an entered salary qualifies for income tax based on a specified threshold using the if..else operator.
# Write a program to determine whether a person can enter a movie theater based on the age restriction using the if..else operator.
# Write a program to determine whether a student is eligible for a scholarship based on marks using the if..else operator.
# Write a program to compare two strings and display whether they are equal or not using the if..else operator.