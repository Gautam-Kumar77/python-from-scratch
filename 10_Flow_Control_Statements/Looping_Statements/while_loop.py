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

