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

#Ex:3 Program for Generating Eve Numbers within N is +VE
n= int(input("Enter a number: "))
if n==0:
    print("Invalid Input!")
else:
    for i in range(2,n+1,2):
        print("\t {}".format(i))