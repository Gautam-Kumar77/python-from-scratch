                                             #LIST

lst= [34,8,3.46,"PYTHON", True]
print(lst, type(lst), id(lst))

print(lst[1])
print(lst[4])

#Item Assignment
lst[1]= 40
lst[4]= False
print(lst)

# Syntax-1:		ListObj=[ Val1 , Val2,....,Val-n]
# Syntax-2:		ListObj=list(Iterable-Object)
# Syntax-3:		ListObj=list( [Iterable-Object] )
# Syntax-4:		ListObj= [Iterable-Object]
# Syntax-5:		ListObj= list([Non-Iterable-Object])
# Syntax-6:		ListObj= [Non-Iterable-Object]

#Syntax 1:
lst1= [34,8+2j,3.46,"PYTHON", True]
print(lst1)

# Syntax-2:
lst1= list("PYTHON")
print(lst1)

r= range(2,21,2)
l= list(r)
print(l)

# Syntax-3:	ListObj=list( [Iterable-Object] )
lst= list(["PYTHON"])
print(lst)

s= "PYTHON"
b= [s]
print(b)

# Syntax- 4: ListObj= [Iterable-Object]
lst4= ["Good Morning"]
print(lst4)

# Syntax-5:	ListObj= list([Non-Iterable-Object])
# a= list(10)
# print(a) # Type Error: 'int' object is not iterable

# Syntax-6:		ListObj= [Non-Iterable-Object]
l= [12]
print(l)