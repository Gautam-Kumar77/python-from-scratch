#Ex:1 program for Demonstrating the Inner Loops
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

# Ex:2 program for Demonstrating the Inner
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

#Ex:3 program for Demonstrating the Inner Loops
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