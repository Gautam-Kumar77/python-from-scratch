                                #TUPLE

# Syntax-1:	tplobj=(Val1,Val2,....,Val-n)
# Syntax-2:	tplobj=Val1,Val2,....,Val-n
# Syntax-3:	tplobj=tuple(IterableObject)
# Syntax-4:	tplobj=tuple([IterableObject])
# Syntax-5:	tplobj=tuple([Non-ItereableObject])
# Syntax-6:	tplobj=(Non-ItereableObject,)
# Syntax-7:	tplobj=(ItereableObject,)

#Empty tuple
t1= ()
t2= tuple()
print(t1)
print(t2)
print(len(t1))


#Non-Empty tuple

t= (23,57,90.4, 89,456,3)
print(t, type(t), id(t))
print(t[1])
print(t[3])
print(t[1:4])
print(t[::-1])
#Item Assignment
# r= t[1]= 58
# print(r)  #TypeError: 'tuple' object does not support item assignment

#syntax:2
tpl= 45,34,7,5,3,245, True
print(tpl,type(tpl))


#Syntax:3
s= "PYTHON"
tp= tuple(s)
print(tp, type(tp))

# tpl= tuple(range(10,21,2)) OR
tpl= range(10,21,2)
r= tuple(tpl)
print(r)

#Conversion
# str to tuple

s1= "Hyderabad"
tup= tuple([s1])
print(tup, type(tup))

lst= [12,34,6,8,6,895]
tupp= tuple([lst])
print(tupp, type(tupp))

#Iterable and Non-Iterable Object
a= 10
# tpl= tuple(a)
# print(t)    #TypeError: 'int' object is not iterable
tpl= tuple([a])
print(tpl)

b= 100
t1= (b,)
print(t1)


                            # Pre-Defined FUnction in Tuple
# tuple support only two function count and index

#index
tup = (12, 34, True, 3+8j, 8.3, 44)
print(tup[2])
print(tup[1])
print(tup.index(True))
print(tup.index(8.3))
# print(tup[6])    #IndexError: tuple index out of range

#count
tup= (10,40,30,20,10,20,30,10,20,10)
print(tup.count(10))
print(tup.count(30))
print(tup.count(100))

#Deep copy is possible but shallow copy is not possible
tup= (10,40,30,20,10,20,30,10,20,10)
tup1= tup
print(tup, id(tup))
print(tup1, id(tup1))

# tup1= tup.copy()   #AttributeError: 'tuple' object has no attribute 'copy'
# del tup[2]  TypeError: 'tuple' object doesn't support item deletion

# VVI
#sorted()
#Syntax:   listobj=sorted(Iterable-object)
#Syntax:   listobj=sorted(Iterable-object,reverse=False)
#Syntax    listobj=sorted(Iterable-object,reverse=True)

t= (2,3,5,6,4,2644,2,12,90)
t1= sorted(t)
print(t1, type(t1))  #<class 'list'>
r= tuple(t1)
print(r, type(r))   #<class 'tuple'>

t1= (22,4,8,333,97,2,99,6,86.6)
z= sorted(t1)
print(z)
z= tuple(sorted(z) [::-1])
print(z)

g= (2,43,24,66,0,111,34)
t= tuple(sorted(g, reverse=True))
print(t)
tp= sorted(g, reverse= False)
print(tp)

# ----------------------------------------------------------------
# Nested of Inner tuple
# ----------------------------------------------------------------

# tuple in tuple
t= (2,4,3,(23,45,21), (34,21,43) )

print(t[2])
print(t.index(2))
print(t[4].index(43))
print(t[4][2])

for val in t:
    print(val, type(val), type(t))

print(max(t[3]))
print(min(t[4]))
# print(max(t))

t1= ((10,20,30),(40,50,60), (70,80,80))
for val in t1:
    print(val)

# list in tuple
tup = (10,20, [1,3,2,7], 87.3, [2,5,9,1], False)
print(tup[1])
print(tup[4][3])
a=tup[4].append(33)
b= tup[2].insert(0, 0)
c= tup[4].sort()

print(tup)
d= tup[4].sort(reverse=True)
print(tup)

#tuple in list
lst= [23,4,(7,9,6), 33.3, (23,67,3)]
print(lst, type(lst))
lst[0]= 2
print(lst)

print(lst[2][0:2])
t= tuple(sorted(lst[2]))
print(t)