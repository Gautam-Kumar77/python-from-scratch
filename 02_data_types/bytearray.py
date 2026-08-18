lst= [123,42,242,11,0,222,126]
b= bytearray(lst)
print(b, type(b))
print(len(lst))

b[1]= 43
b[6]= 20
print(b)

for i in b:
    print(i)

print(b[1])

for k in b[0:4]:
    print(k)
