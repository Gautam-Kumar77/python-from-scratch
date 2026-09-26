                                        #BREAK

# Ex:1 Program for Demonstrating break keyword
s= "PYTHON"
for i in s:
    if i=="H":
        break
    print(i)

# Ex:2 Program for Demonstrating break keyword display Only PYTH without using Slicing and Indexing
s= "PYTHON"
i=0
while(i<=len(s)):
    if s[i]=="T":
        break
    print("{}".format(s[i]),end="")
    i= i+1

# Ex:3 Program for accepting a Numerical Integer Value and  Decide whether It  is Prime or not
n= int(input("Enter a number: "))
if n<=1:
    print("Invalid Input!")
else:
    res= "PRIME"
    for i in range(2, n):
        if n%2==0:
            res= "NOT PRIME"
            break
    print("\t{} is {}".format(n, res))