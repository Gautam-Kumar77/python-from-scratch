                                    #frozenset

#it is immutable, doesnt maintain insertion order, used to freez the set, Duplicate are not allowed

#Empty frozenset
fz= frozenset()
print(fz, len(fz))

#Non Empty frozenset
s= {28,3,6,8,3,3+4j, 90.3, True}
print(s)
fz1= frozenset(s)
print(fz1)

fz2=frozenset({True, "Hello", 8})
print(fz2)
# fz2[0]    #TypeError: 'frozenset' object is not subscriptable
# fz2[0:3]    #TypeError: 'frozenset' object is not subscriptable
# fz2[1]=33   #TypeError: 'frozenset' object does not support item assignment

#del operator
# del fz2[2]  TypeError: 'frozenset' object doesn't support item deletion
# del fz2[1:2]  TypeError: 'frozenset' object doesn't support item deletion
del fz2
