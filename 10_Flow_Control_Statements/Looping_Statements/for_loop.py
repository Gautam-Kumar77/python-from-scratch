#Ex:1 Program for Generating 1 to N where N is +VE
n= int(input("Enter a number: "))
if n<=0:
    print("Invalid Input!")
else:
    for i in range(1, n+1, 1):
        print(i)
    else:
        print("="*50)

#Ex:2 Program for Generating N to 1 where N is +VE
n= int(input("Enter a number: "))
for i in range(n, 0, -1):
    print(i)

#Ex:3 Program for Generating Even Numbers within N is +VE
n= int(input("Enter a number: "))
if n==0:
    print("Invalid Input!")
else:
    for i in range(2,n+1,2):
        print("\t {}".format(i))

#Ex:4 Program for Finding Sum of Digits of a +ve Number
n= int(input("Enter a number to sum"))
total=0
for i in range(1, n+1, 1):
    total= total+i
print(total)

#Ex:5 Program for Accepting List of Values from Key Board and display
n= int(input("Enter a number how many numbers you want to store: "))
if n<=0:
    print("Invalid Input!")
else:
    lst= list()
    for i in range(1, n+1):
        val= float(input("Enter {} values".format(i)))
        lst.append(val)
    else:
        print("Values are: ")
        print(lst)

#Ex:6 Program for Cal sum Squares and Cubes  of N Natural Nums
n= int(input("Enter a number: "))
if n<=0:
    print("Invalid Input!")
else:
    total=0
    total1=0
    total2=0
    for i in range(1, n+1):
        total= total+i
        total1= total1 + i**2
        total2= total2 + i**3
    print("Sum of total number is: {}".format(total))
    print("Square of total number is: {}".format(total1))
    print("cube of total number is: {}".format(total2))
    print()

# Ex:7 Program for Cal Product  of N Natural Nums
n= int(input("Enter a number: "))
if n<=0:
    print("Invalid Input: ")
else:
    pd= 1
    for i in range(1, n+1):
        pd= pd*i
    print(pd)

#Ex:8 Program for Accepting List of Values from Key Board and Find their sum and average
n= int(input("Enter a number to store values"))
if n<=0:
    print("Invalid Input!")
else:
    total= 0
    lst= list()
    avg= 0
    for i in range(1, n+1):
        val= float(input("Enter value {}:- ".format(i)))
        total= total+val
        avg= total/n
        lst.append(val)
    print("Values are here: ")
    print(lst)
    print("Sum is: ", total)
    print("Average is:{}".format(avg))

#Ex:9 program for Cal Factorial of a Number
n= int(input("Enter a number: "))
if n<= 0:
    print("Invlid Input.")
else:
    fact= 1
    # total=0
    for i in range(n, 0, -1):
        fact= fact*i
        # total= fact+i
    print(fact)