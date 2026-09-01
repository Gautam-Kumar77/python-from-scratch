                                        #dict

#Values of keys are immutable but values are mutable

#Empty dict
objdct1= {}
print(objdct1, type(objdct1))

dctobj= dict()
print(dctobj, type(dctobj))


#NonEmpty dict
dct= {
    "Name" : "TATA",
    "Age" : 24,
    "Course": 'MCA'
}
print(dct, type(dct))
print(dct.get("Name"))
print(dct["Name"])

for k,v in dct.items():
    print(k, "-->", v)

# print(dct["Python"]) #KeyError: 'Python'
dct["Roll"]= 78
dct["Age"]= 30
print(dct)


#Predefined functions in dict

#1. clear()
d= { 10:1.2, 20: 2.4, 30:3.5, 40: 4.9}
for k,v in d.items():
    print(k,v)

d.clear()
print(d, len(d))

#2. copy()
d= { 10:1.2, 20: 2.4, 30:3.5, 40: 4.9}
x= d.copy()
print(x, id(x), id(d))  #Shallow Copy

d1=d
print(d1, id(d1), id(d)) #Deep Copy

#3. pop(key)
d= { 10:1.2, 20: 2.4, 30:3.5, 40: 4.9}
print(d.pop(20))
# print({}.pop(1000))  #KeyError: 1000
# print(dict().pop(90))   KeyError: 90
print(d)

#4. popitem()     used to remove last item from dict
d= { 10:1.2, 20: 2.4, 30:3.5, 40: 4.9}
print(d.popitem())
print(d)

#5. get()
d= {"Name" : "TATA", "Age" : 24, 45:89.4}
print(d.get(45))
print(d.get("Name"))
print(d.get(909309))     #None
# print(d[90993])         #KeyError: 90993

#6. keys()
d= {"Name" : "TATA", "Age" : 24, 45:89.4, 8:3+0j}
print(d.keys())   #dict_keys(['Name', 'Age', 45, 8])

for k in d.keys():
    print(k, "-->" , d.get(k))

for ks in d.keys():
    print(ks, "-->", d[ks])

#7. values()
d= {"Name" : "TATA", "Age" : 24, 45:89.4}
print(d.values())

for i in d.values():
    print(i)

#5. items()

d= {"Name" : "TATA", "Age" : 24, 45:89.4, "val" :True}
print(d.items())

for val in d.items():
    print(val)

for val in d.items():
    print(val[0], "----->", val[1])

for k,v in d.items():
    print(k , "-->", v)

#9 update()

d1= {10:1.2, 20:2.3}
d2= {30:1.2, 40:2.3}
x1= d1.update(d2)
print(d1, type(d1))

d3= {10:1.2, 20:2.3}
d4= {30:1.2, 40:2.3}
x2= d4.update(d3)
print(d4)


