                                #EASY
#1. Accept a number n and print numbers from 1 to n.
# n= int(input("Enter a Number: "))
# if n<=0:
#     print("Invalid Input!")
# else:
#     i = 1
#     while i<=n:
#         print(i)
#         i=i+1
#     else:
#         print("="*40)
# print("Program Executed Successfully...")
#
# #2. Accept a number n and print numbers from n down to 1.
# n= int(input("Enter a Number: "))
# if n<=0:
#     print("Invalid input")
# else:
#     while n>=1:
#         print(n)
#         n= n-1
#     else:
#         print("Loop Executed Successfully")
#
#
# #3. Accept a number n and print the first n natural numbers.
# n= int(input("Enter a Number: "))
# if n<=0:
#     print("Invalid Input")
# else:
#     i=1
#     while i<=n:
#         print(i)
#         i=i+1
#     else:
#         print("Loop Executed Successfully")
# print("Exited")
#
# #4. Accept a number n and print its multiplication table from 1 to 10.
# n= int(input("Enter a number to print table: "))
# if n==0:
#     print("Invalid Input!")
# else:
#     i=1
#     while i<=10:
#         print(n , "*", i, "=", n*i)
#         i= i+1
#     else:
#         print("Table printed successfully!")
# print("Exited")
#
# #5. Accept a number n and print all even numbers from 1 to n.
# n= int(input("Enter a number to print Even numbers: "))
# if n<=0:
#     print("Invalid Input!")
# else:
#     i=1
#     while i<=n:
#         print(i)
#         i= i+2
#     else:
#         print("Even Number printed successfully!")
# exit()

                                         #MEDIUM

#6.Accept a number n and print all odd numbers from 1 to n.
# n= int(input("Enter a number to print Odd numbers: " ))
# if n<=0:
#     print("Invalid Input!")
# else:
#     i=1
#     while i<=n:
#         print(i)
#         i= i+2
#     print("Odd Number printed successfully!")
# exit()

#7. Accept a number n and print the square of every number from 1 to n.
# n=int(input("Enter a number to print Square of every numbers: " ))
# if n<=0:
#     print("Invalid Input!")
# else:
#     i=1
#     while i<=n:
#         print(i , "^", i, "=", i**2)
#         i= i+1
#     else:
#         print("Square of every number executed Successfully!")
# exit()

#8. Accept a number n and print the following:
# 5
# 4
# 3
# 2
# 1
# But do not modify n. Use another variable as the counter.
# num=int(input("Enter a number: "))
# if num<=0:
#     print("Invalid Input!")
# else:
#     t=num
#     while(1<=t):
#         print(t)
#         t= t-1
#     print("Executed Successfully")

#9 Accept a number n and print:

# 1 * 5 = 5
# 2 * 5 = 10
# 3 * 5 = 15
# 4 * 5 = 20
# 5 * 5 = 25
# for input 5.

# num=int(input("Enter a number: "))
# if num<=0:
#     print("Invalid Input!")
# else:
#     i= 1
#     while i<=num:
#         print(i, "*", num, "=", i*num)
#         i= i+1
#     else:
#         print("Executed Successfully!")

#10. Accept a number n and print the numbers from n to 1, along with their squares.
num=int(input("Enter a number: "))
if num<=0:
    print("Invalid Input!")
else:
    t=num
    while t>=1:
        print(t, '->', t**2)
        t= t-1