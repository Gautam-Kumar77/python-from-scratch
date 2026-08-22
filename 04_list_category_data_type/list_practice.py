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

#PreDefined functions in List

#1. append()
lst4= [34,8+2j,3.46,"PYTHON", True]
print(lst4, type(lst4), id(lst4))
lst4.append(False)
lst4.append("Hyderabad")
print(lst4, type(lst4), id(lst4))

#2 extend() used to add multiple elements at the end
lst4= [34,8+2j,3.46,"PYTHON", True]
lst4.extend([101,102])
print(lst4)

#3 insert()  used to add the value at the specified index
lst4= [34,8+2j,3.46,"PYTHON", True]
lst4.insert(2, 100)
print(lst4)

lst4.insert(-2, "Hello")   # insert "Hello before the element at index -2"
print(lst4)

lst4.insert(100, 21.2)
print(lst4)

#4 remove()   used to remove first occurence of specified value from list object
lst4= [34, (8+2j), 100, 3.46, 'Hello', 'PYTHON', True, 21.2]
lst4.remove(21.2)
print(lst4)

l= [10,20,10,10,20,30,30,10,20]
l.remove(30)
print(l)

# l.remove(100)
# print(l)  #ValueError: list.remove(x): x not in list

#5 pop() Based on index(used for removing the value from the list based on index)
l= [10,20,10,10,20,30,30,10,20]
l.pop(-2)
print(l)
# l.pop(100)  #IndexError: pop index out of range
# list().pop(0)  #IndexError: pop from empty list
# [].pop(-1) #IndexError: pop from empty list

l.pop() # it will remove last element from a list
print(l)

#6 clear()  it used to remove all the elements from list
l= [10,20,10,10,20,30,30,10,20]
l.clear()
print(l)

