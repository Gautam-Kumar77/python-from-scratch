#Ex:1 Write a program to demonstrate nested for loops (1–5 and 1–3).
print("="*40)
print("Program for Nested Loop using for loop")
print("="*40)
for i in range(1, 6):
    print("Outer Loop: {}".format(i))
    print("="*15)
    for j in range(1,4):
        print("Inner Loop: {}".format(j))
    else:
        print("-------------------------------------------------")
else:
    print("I am from outer loop else")

# Ex:2 Write a program to demonstrate nested while loops (1–5 and 1–3)
print("="*40)
print("Program for Nested Loop")
print("="*40)
i=1
while i<=5:
    print("Outer Loop {}".format(i))
    print("="*20)
    j=1
    while j<=3:
        print("Inner Loop {}".format(j))
        j= j+1
    else:
        i = i + 1
        print("----------------------------------------------")
else:
    print("Im outside inner loop")

#Ex:3 Write a program using while inside for with outer loop 1–4 and inner loop 1–2.
print("="*40)
print("Program for Nested Loop")
print("="*40)
i=5
while i>=1:
    print("Outer Loop {}".format(i))
    print("="*20)

    for j in range(4,1,-1):
        print("Inner Loop {}".format(j))

    else:
        i = i - 1
        print("--------------------------------------------")

#Ex4: Write a program using for inside while with outer loop 5–1 and inner loop 4–2.
for i in range(1,5):
    print("Outer loop: {}".format(i))
    print("="*15)

    j=1
    while j<=2:
        print("Inner Loop {}".format(j))
        j= j+1
    else:
        print("---------------------------")

#Ex5: Program for Generating 1 to N Mul Tables where N is +VE
n= int(input("Enter How Many Mul Tables u want to Generate: "))
for i in range(1,n+1):
    print("Table of {}".format(i))
    print("="*20)
    for j in range(1,11):
        print(i ,"*", j, "=", i*j)
    else:
        print("----------------------------")

# Ex6: PRIME
n= int(input("Enter a number: "))
for i in range(2, n+1):
    res= True
    for j in range(2,i ):
        if i%j==0:
            res= False
            break
    if(res):
        print("\t{}".format(i))
else:
    print("--------------------------------")

# Ex:7 Program for accepting age of Citizen and Decide Whether Citizen is Eligible to Vote OR Not
while(True):
    n= int(input("Enter Your Age: "))
    if n>=18:
        print("You are Eligible to Drive")
        break
    else:
        print("You are not Eligible for Drive")

# Ex8: Program for accepting List of Values and Find Max and Min
n= int(input("Enter how many number of list you want: "))
if n<=0:
    print("Invalid Input!")
else:
    lst= list()
    for i in range(1, n+1):
        val= float(input("Enter number {}: ".format(i)))
        lst.append(val)
    print("Values are: ",lst)
    print("Minimum No:-", min(lst))
    print("Maximum No:-", max(lst))
print("Program Executed Successfully")


#Ex9: Program for accepting List of Values and Find Max and Min
n= int(input("Enter a number how many values you want to store: "))
if n<=0:
    print("Invalid Input!")
else:
    lst= list()
    for i in range(1,n+1):
        val = float(input("Enter number {}: ".format(i)))
        lst.append(val)
    else:
        print("Values are: ",lst)
        maxv= lst[0]
        for val in lst[1:]:
            if val>maxv:
                maxv=val
        else:
            print("Maximum value is: ",maxv)
            minv= lst[0]
            for val in lst[1:]:
                if val<minv:
                    minv= val
            else:
                print("Minimum Value: ", minv)
print("Program Executed Successfully")

