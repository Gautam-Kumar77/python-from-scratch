# -----------------------SET------------------------
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
s= "PYTHON"
st= set(s)
print(s, id(s))

s= "MISSISSIPI"
st1= set(s)
print(s, id(s))

