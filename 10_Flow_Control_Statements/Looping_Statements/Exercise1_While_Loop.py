#1. Accept a number n and print numbers from 1 to n.
n= int(input("Enter a Number: "))
if n<=0:
    print("Invalid Input!")
else:
    i = 1
    while i<=n:
        print(i)
        i=i+1
    else:
        print("="*40)
print("Program Executed Successfully...")

#2. Accept a number n and print numbers from n down to 1.
n= int(input("Enter a Number: "))
if n<=0:
    print("Invalid input")
else:
    while n>=1:
        print(n)
        n= n-1
    else:
        print("Loop Executed Successfully")


#3. Accept a number n and print the first n natural numbers.
n= int(input("Enter a Number: "))
if n<=0:
    print("Invalid Input")
else:
    i=1
    while i<=n:
        print(i)
        i=i+1
    else:
        print("Loop Executed Successfully")
print("Exited")

#4. Accept a number n and print its multiplication table from 1 to 10.
n= int(input("Enter a number to print table: "))
if n==0:
    print("Invalid Input!")
else:
    i=1
    while i<=10:
        print(n , "*", i, "=", n*i)
        i= i+1
    else:
        print("Table printed successfully!")
print("Exited")

#5. Accept a number n and print all even numbers from 1 to n.
n= int(input("Enter a number to print Even numbers: "))
if n<=0:
    print("Invalid Input!")
else:
    i=0
    while i<=n:
        print(i)
        i= i+2
    else:
        print("Even Number printed successfully!")
exit()

#6.Accept a number n and print all odd numbers from 1 to n.