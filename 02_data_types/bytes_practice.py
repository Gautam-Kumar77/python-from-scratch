a= [123,23, 43, 129, 205, 0, 255]
b= bytes(a)
print(a)
print(b)  #b'{\x17+\x81\xcd\x00\xff'


a[1]=24
print(a)
print(b)

b[2]=25;
print(b)  #TypeError: 'bytes' object does not support item assignment

# bytes is a immutable