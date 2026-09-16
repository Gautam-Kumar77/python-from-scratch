#1 capitalize()
from pickletools import string1

s= "python"
print(s,id(s))
print(s.capitalize(), id(s))

s= "python is a Programming Lang."
print(s.capitalize())

#2 title()
s= "python is a programming lang."
print(s.title())

s= "123pyth45"
print(s.title())

#3 count()
s= "MISSISSIPI"
print(s.count("S"))
print(s.count("M"))

#4 swapcase()
s= "pYtHoN"
print(s.swapcase())

s1= "python"
print(s1.swapcase())

#5 index()
s= "Java"
print(s.index("J"))

for i,v in enumerate(s):
    print(i, "-->", v)

s1="MISSISSIPI"
for i,v in enumerate(s1):
    if (v=="I"):
        print(i, "-->", v)

#6 find()   --Returns first occurence
s="MISSISSIPI"
print(s.find("S"))
print(s.find("I"))
