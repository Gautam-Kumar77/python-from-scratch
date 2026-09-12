                        #Bitwise left shift operator

print(10<<3)
print(4<<3)
print(10<<0)
print(-2<<4)
# print(10.3<<3)  #TypeError: unsupported operand type(s) for <<: 'float' and 'int'
# print(4<<-1)     ValueError: negative shift count

                        #Bitwise right shift operator

print(10>>3)
print(32>>3)
print(32>>2)
print(20>>0)
print(-10>>3)
# print(12.3>>3)   TypeError: unsupported operand type(s) for >>: 'float' and 'int'
# print(23>>-3)   ValueError: negative shift count

                        #Bitwise OR operator

#eg1
print(1|0)
print(1|1)
print(0|1)
print(0|0)

#eg2
a=5
b=4
print(a|b)
print(10|15)
# print(1.2|2.4)    TypeError: unsupported operand type(s) for |: 'float' and 'float'

#eg3
s1= {2,3,5}
s2= {5,6,8}
s3= s1|s2
print(s3)

print(set("PYTHON") | set("NISSON"))
lst1= [2,3,9]
lst2= [8,7,9]
print(set(lst1) | set(lst2))

