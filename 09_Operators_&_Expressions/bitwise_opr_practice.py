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

                                #Bitwise AND Operator

#eg1
print(1&0)
print(0&1)
print(0&0)
print(1&1)

#eg2
print(10&4)
print(5&4)
print(20&25)

#eg3
s1={10,20,30}
s2={30,40,50}
s3= s1&s2
print(s3)

                            #Bitwise complement operator(~)

print(12)
print(~12)

                            #Bitwise XOR Operator(^)

#eg1
print(0^0)
print(0^1)
print(1^0)
print(1^1)

#eg2
print(4^5)
print(10^15)
print(4^6)

#Swapping
a=2
b=3
print(a, b)
a=a^b
b= a^b
a= a^b
print(a,b)

#eg3
s1={2,3,4}
s2={4,5,6}
s3= s1^s2
print(s3)

print({10,20,30}^{30,40,50})
print({10,20}^{20,10})