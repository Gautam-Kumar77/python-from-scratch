# Ex1. program for accepting any value and Decide whether It is Palindrome or not
val= input("Enter a value")
if val==val[::-1]:
    print("{} is Palindrome".format(val))
else:
    print("{} is not palindrome".format(val))

# Ex2. Program for accepting any Numerical value and Decide whether It is +VE or -VE or Zero
n= int(input("Enter a numerical value"))
if n>0:
    print("It is +ve number.")
elif n==0:
    print("It is Zero")
else:
    print("It is -VE number")
print("Program Execution Completed")

# Ex 3. Program for accepting any +VE Numerical Integer Value and decide whether It is Even OR Odd
num= int(input("Enter a number: "))
if num>0 and num%2==0:
    print("{} is +ve number and {} is Even number:".format(num, num))
else:
    if (num>0) and (num%2!=0):
        print("It is Negative Number and it is odd number")
    else:
        print("Invalid Input")
print("Program executed successfully")

# Ex4. program for Cal SI By accepting P,T and R Values
p= int(input("Enter Principle: "))
r= int(input("Enter rate: "))
t= int(input("Enter Time: "))

if p>0 and r>0 and t>0:
    si= (p*r*t)/100
    print("Simple interest is:-", si)
else:
    if p <= 0:
        print("Invalid Principle")
    if r <= 0:
        print("Invalid Rate")
    if t <= 0:
        print("Invalid Time")

#Ex5. Program for accepting and display Its Name
d=int(input("Enter Any Digit:")) # 0  1  2 3  4 5 6 7 8 9
if(d==0):
    print("\t{} is ZERO".format(d))
else:
    if (d == 1):
        print("\t{} is ONE".format(d))
    else:
        if (d == 2):
            print("\t{} is TWO".format(d))
        else:
            if (d == 3):
                print("\t{} is THREE".format(d))
            else:
                if (d == 4):
                    print("\t{} is FOUR".format(d))
                else:
                    if (d == 5):
                        print("\t{} is FIVE".format(d))
                    else:
                        if (d == 6):
                            print("\t{} is SIX".format(d))
                        else:
                            if (d == 7):
                                print("\t{} is SEVEN".format(d))
                            else:
                                if (d == 8):
                                    print("\t{} is EIGHT".format(d))
                                else:
                                    if (d == 9):
                                        print("\t{} is ZERO".format(d))
                                    else:
                                        if(d>9):
                                            print("\t{} is +VE Number".format(d))
                                        else:
                                            if(d<0) and d in range(-1,-10,-1):
                                                print("\t{} is -VE Digit".format(d))
                                            else:
                                                print("\t{} is -VE Number".format(d))
print("Program Execution Completed")
