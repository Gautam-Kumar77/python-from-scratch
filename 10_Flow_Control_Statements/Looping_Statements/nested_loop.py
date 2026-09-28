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