                        #set combinations with set,list,tuple,dict

# CASE 1: set in set    :  bcoz a normal set is mutable
# st= {3,5,{34,37,31}, 9, 8}
# print(st[3])  #TypeError: cannot use 'set' as a set element (unhashable type: 'set')
# print(st)      #TypeError: cannot use 'set' as a set element (unhashable type: 'set')


# CASE 2: list in set  :IMPOSSIBLE because list is mutable
# st1= {3,4,9, [9,4,10], 10,40}
# print(st1)    #TypeError: cannot use 'set' as a set element (unhashable type: 'set')


# CASE 3: tuple in set :POSSIBLE, because tuple is immutable
st2= {12,5,6,(90,100,70), 89}
print(st2)

for i in st2:
    print(i)

# CASE 4: dict in set  :NOT Possible, bcoz dict is mutable and dict can can contain immutable object
std= {23,4, {'md':23, 'rs': 67, 8:23}, "Python", 89}
print(std)


