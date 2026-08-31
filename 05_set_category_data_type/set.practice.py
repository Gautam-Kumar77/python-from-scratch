# -----------------------SET------------------------
from operator import rshift
from uuid import uuid3

s= {2,4,53,12,555,74}
print(s, type(s))

# Indexing and slicing is not possible in set Data type
# e= s[0]
# sl= s[2:5] TypeError: 'set' object is not subscriptable
# print(e)
# print(sl)  TypeError: 'set' object is not subscriptable

# set data type doesnt support item assignment
# s[1]=2
# print(s)  TypeError: 'set' object does not support item assignment

#Duplicate value not allowed
s1= "PYTHON"
st= set(s1)
print(s1, id(s1))

s2= "MISSISSIPI"
st1= set(s2)
print(st1, id(s2))

lst= [3,4,73,97,12]
st3= set(lst)
print(st3)

#Predefined Functions in set
# -----------------------------------------
#1. add()
s1= {10, "RS", 45.32, "Python"}
s1.add(45)
print(s1)

empSet= set()
empSet.add(12)
empSet.add(902)
empSet.add("Python")
print(empSet, type(empSet))

#2. remove()
s1.remove(10)
print(s1)

# s1.remove(922)
# print(s1)        #KeyError: 922

#3. discard()
s1.discard(45.32)
print(s1)
print("Helo")
s1.discard(100)
print("Hii")

spt= {234,4,2,90,"Rossum", 12}
print(spt)
spt.discard(4)
print(spt)

#4. pop
sp= { 34, 23, 56}
sp.pop()
print(sp)
sp.pop()
print(sp)

#5. clear
sc= { 74,32,45,24,13}
sc.clear()
print(sc, type(sc))
op = len(sc)
print(op)

#6. copy
ele= {4,3,43}
tp= ele.copy()    #Shallow Copy
print(tp)
tp1= tp           #Deep copy
print(tp1)

#7. isdisjoint()
s1= {10,20,30,40}
s2= {10,15,25,35}
s3= {18,28,38,8}

p= s1.isdisjoint(s2)
p1= s1.isdisjoint(s3)
p2= s2.isdisjoint(s3)
print(p)
print(p1)
print(p2)

print(set("python").isdisjoint('hello'))
print(set("python").isdisjoint('fizz'))

#8 issuperset
a= {10,20,30,40}
b= {10,23,12}
c= {10, 30}

print("Good Morning!")
a1= a.issuperset(b)
c1= a.issuperset(c)
uno= c.issuperset(a)
print(a1)
print(c1)
print(uno)

#9 issubset
a= {10,20,30,40}
b= {10,23,12}
c= {10,30}

sub= c.issubset(a)
print(sub)

sub1= b.issubset(a)
print(sub1)

eg= set().issubset({8,43,2})
print(eg)
print(set().issubset(set()))

#10 Union
u1= {10,20,30,40}
u2= {30,50,60}
u3= {80,90,100}

re= u1.union(u2)
print(re)
print(u1.union(u3))

s= "Python"
s1= "java"
print(set(s).union(set(s1)))

#11 intersection()

s1= {10,20,30,40}
s2= { 30,40,50,60}
s3= s1.intersection(s2)
print(s3)

s4= {20,30,60}.intersection({20,40,50})
print(s4)

lst= [10,20,30,40]
lst1= [30,40,50,60]

# s1= lst.intersection(lst1)
# print(s1)   AttributeError: 'list' object has no attribute 'intersection'
s= set(lst).intersection((set(lst1)))
print(s, type(s))

#12 difference()
s1= {10,20,30,40}
s2= { 30,40,50,60}
diff= s1.difference(s2)
diff1= s2.difference(s1)

print(diff)
print(diff1)

#13 symmetric_difference()
s1= {10,20,30,40}
s2= { 30,40,50,60}
sdiff= s1.symmetric_difference(s2)
print(sdiff)

s1diff= {1,2,3}.symmetric_difference({8,9,0})
print(s1diff)

s2diff= {1,2,3}.symmetric_difference({1,2,3})
print(s2diff)

#14 update()      used for adding or merging the content of s2 with s1 itself
s1= {10,20,30,40}
s2= {10,20,30,60}
s3= s1.update(s2)
print(s1)
print(s3)  #None

#15  difference_update()
s1= {10,20,30,40}
s2= {30,40,50,60}
s3= s1.difference_update(s2)
print(s1)

s4= s2.difference_update(s1)
print(s2)

#16 intersection_update()
s1= {10,20,30,40}
s2= {30,40,50,60}
inup= s1.intersection_update(s2)
print(s1)

#17 symmetric_difference_update()
s1= {10,20,30,40}
s2= {30,40,50,60}
sdu= s1.symmetric_difference_update(s2)
print(s1)


  #Combination of set with set, list , tuple

#CASE 1: set in set  :NOT POSSIBLE
# s= {23,5,24,{3,5,8}, {4,9,0,1}, "Hello"}
# print(s, type(s))

#CASE 2: list in set   :NOT POSSIBLE
# s= {23,5,24,[3,5,8], [4,9,0,10], "Hello"}
# print(s, type(s))

#CASE 3: tuple in set   :POSSIBLE bcoz tuples are immutable
s= {23,5,24,(3,5,8), (4,9,0,1), "Hello"}
for i in s:
    print(i, type(i), type(s))

#CASE 4: set in list
lst= [34,6,{8,6,4}, 78, "PYTHON",{2,4,1}]
lst[2]=43
print(lst,type(lst))
for i in lst:
    print(i, type(i))

#CASE 5: set in tuple
tpl= (32,45,3,{55,8,33}, 9.8)
tpl[3].discard(8)
tpl[3].add(1200)
for i in tpl:
    print(i)
