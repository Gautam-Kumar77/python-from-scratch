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