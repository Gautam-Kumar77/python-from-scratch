#Ex1: Program for Generating 1 to N where N is +VE#Program for Generating 1 to N where N is +VE
n= int(input("Enter +ve number: "))
i= 1

if i<=0:
    print("Invalid Input: ")
else:
    print("="*50)
    print("Numbers Within:- {} ".format(n))
    while(i<=n):
        print(i)
        i= i+1
    else:
        print("="*50)
    print("Program Executed Successfully.")

#Ex2: Program for Generating N to 1 where N is +VE
n= int(input("Enter a number for Generate"))
if n<=0:
    print("Invalid Input")
else:
    i=1
    while n>=i:
        print(n)
        n= n-1

#Ex:3 Program for Generating all even Numbers within N
n= int(input("Enter a number"))
if n<=0:
    print("Invalid Input.")

else:
    i=2
    while i<=n:
        print(i)
        i=i+2
    else:
        print("="*50)

#Ex:4 Program for Generating all even Numbers within N
n = int(input("Enter a number:  "))
if n<=0:
    print("Invalid Input")
else:
    i=1
    while(i<=n):
        if i%2==0:
            print(i)
        i= i+1
    print("="*50)
print("Program Executed Successfully")

#Ex5:
n= int(input("Enter a number: "))
while(1<=n):
    print(n)
    n= n-2
else:
    print("="*50)