from pygments.lexers.sql import re_error  #LIST

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
#NOTE: Alternatively, we can Use an Operater + for Concatinating of Two OR More List Object and Conatinating Results
#placed in New List with Different Memory Address.

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



# NOTE:-                                  #del Operator

lstt= [45,23,78,222,"Python", True]
del lstt[3]
print(lstt)

lstt= [67,23,21,355,"Hello"]
del lstt[1:3:1]
print(lstt)

lstt= [3848,45,24,2.66, 6.4, False]
del lstt


#7. index()   used to find first occurence of specified value
l1= [20,22,20, False, 45,76,34.21,3+9j, "Hii", False]
print(l1.index(76))
print(l1.index(0))
print(l1.index(False))


                                            #enumerate()

#used for finding indexes and corresponding values of any iterable object
#NOTE
l2= [10, 20, 30,10, 20,10,30,40]
for index, value in enumerate(l2):
    print(index, "---->", value)

for index, value in enumerate(l2):
    if value==10:
        print(index,"---->", value)

# l1= 123
# for i in enumerate(l1):  #TypeError: 'int' object is not iterable
#     print(l1)

#8. count()  used to count the number of occurences of specified values

l2= [10, 20, 30,10, 20,10,30,40]
print(l2.count(10))
print(l2.count(100))   # it will return 0 bcoz 100 is not in the list
#NOTE
# print(list("1234123467").count(1))   # it will return 0 bcoz 1 is not in the list, Here "1234123467" is str
print(list("12341234267").count("2"))
print(['12341234267'].count("123"))     #0
# print(list["12341234267"].count("123"))  #TypeError: descriptor 'count' for 'list' objects doesn't apply to a 'str' object
print((["12341234267"])[0].count("123"))

#9 copy()          Return a shallow copy of the list.
#1. Shallow Copy       2. Deep Copy

#1. Shallow Copy
lst1= [10,20,30]
lst2=  lst1.copy()
print(lst1, id(lst1))
print(lst2, id(lst2 ))

lst1.append(40)
lst2.insert(3, 50)
print(lst1, id(lst1))
print(lst2, id(lst2 ))

#2. Deep Copy

ls1= [23,44,33,22]
lst2=lst1
print(lst1, id(lst1))
print(lst2, id(lst2 ))

lst1.append(100)
print(lst1, id(lst1))
print(lst2, id(lst2 ))

#10.. reverse() it is used to reverse elements in such a way that back elements comes to front and front goes to back
l3= [23,2,6,565,True, 1.0, 2+4j, False]
l2= l3.reverse()
print(l3)
print(l3[::-1])

#11. sort()
# Syntax-1:		ListObj.sort()----------------------->Sorts the Data in Ascending Order
# Syntax-2:		ListObj.sort(reverse=False)----->Sorts the Data in Ascending Order
# Syntax-3:		ListObj.sort(reverse=True)------>Sorts the Data in Descending Order

l4 = [23,4,56,13,7,2,1,99,568]
l5=l4.sort()
print(l4)

l51= l4.sort(reverse= True) # It will print the value in descending order
print(l4)

# l6= [23,"Tree", 4.3, True]
# l52= l6.sort()
# print(l6)  #TypeError: '<' not supported between instances of 'str' and 'int'


                               #NESTED LIST OR INNER LIST

print("Matrix")
nested= [23, "Matrix", [23,34,56], [83,45], 344, 3.23, True]
print(nested)

print(nested[2][1])
print(nested[-5][-2])

for index, value in enumerate(nested):
    print(index, '--->', value)


mat= [[10,20,30], [40,50,60], [70,80,90]]
for i in mat:
    print(i)

mat3d= [[[10,20, 30], [40,50,60]] , [[70,80,90], [100,110,120]]]
for top in mat3d:
    for row in top:
        print(row)

print(len(mat3d))
print(mat3d[1][1][0])
mat3d[1][0][1]=800

mat3d[0][1][2]=70
print(mat3d)

