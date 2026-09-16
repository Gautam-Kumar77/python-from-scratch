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
print(s.find("L"))

print(s.index("M"))
# print(s.index("L"))   ValueError: substring not found

#If we want last occurence, then
print(s.rfind("I"))
print(s.rindex("I"))

#7 lower()
s= "PYTHON"
print(s.lower())

#8 upper()
s= "python"
print(s.upper())

#9 isupper()
s= "PYTHON"
print(s.isupper())

s1= "PyTHon"
print(s1.isupper())

n= "123"
print(n.isupper())

#10 islower()
s= "PYTHON"
print(s.islower())

s1= "PyTHon"
print(s1.islower())

n= "123"
print(n.islower())

s2= "python"
print(s2.islower())

#11 isalpha()
s= "Hyderabad"
print(s.isalpha())
