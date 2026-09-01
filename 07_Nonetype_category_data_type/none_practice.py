                                    #None

a= None
print(a, type(a))
print(None==0)    #False
print(None==False)   #False
print(None=="")     #False
print(None==None)   #True

print({}.clear())    #None
print(set().clear())    #None
print([].clear())   #None

d2= {89:23,43:456,"Hello":89, 90.32:899}
d22= d2.get(89)
print(d2)
print(d22)