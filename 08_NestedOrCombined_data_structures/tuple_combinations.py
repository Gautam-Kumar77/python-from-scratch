                            #tuple combinations with list, tuple, set , dict

#1. tuple in tuple
tpl=(10, "Guido Van Rossum", (4,74,3), 7.6, (54,86,10))
print(tpl[0])
print(tpl[2])
print(tpl[-1])
print(tpl[1:3])

print(max(tpl[2]))

for var in tpl:
    print(var)

#2. list in tuple
tpl= (3,8, [10,20,15,5], 90)
print(tpl[2])
print(tpl[3])
print(tpl[2][::-1])

sr=tpl[2].sort()
print(tpl)

tplx= tpl[2].append(100)
print(tpl)

#3. set in tuple
lst= ("Morning", 34, {3,6,8,3}, True, {4,10,8})
print(lst[2])

st= lst[2].remove(3)
print()

st1= lst[-1].add(20)
print(lst)

#dict in tuple
tpl= (34,45,{3:10, 2:20,1:10}, False, {"a":12, "b":23})
print(tpl)
print(tpl[4])

for val in tpl:
    print(val)
dt= tpl[2].pop(1)
print(tpl)

for k,v in tpl[2].items():
    print(k,"-->", v)
