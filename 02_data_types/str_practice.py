#Single Line String Data
s1= "Python"
print(s1, type(s1))
s1= 'Python'
s2= 'A'
s3= "123123"
s4= "addr23"
s5="@#987"
print(s1,s2,s3,s4,s5)

singleLine= """Good Morning, Jarvis"""
print(singleLine, type(singleLine))

#Multi Line String Data
multiLine= ('''Guido Van Rossum,
            HouseNo:- 12, Banjara Hills,
            Hyderabad, India,
            500034'''
            )
print(multiLine, '\n', type(multiLine))


# String Indexing and Slicing

#INDEXING
st= "PYTHON"
print(st, type(st))
print(st[True])
print(st[False])
print(st[-True])
print(st[4])
print(st[-len(st)])
# print(st[len(st)]) IndexError
# print(st[2.4]) TypeError
# print(st[6]) IndexError

#SLICING

# CASE 1. +ve BEGIN: +ve END
st1 = "PYTHON"
print(st1[1:4])
print(st1[2:5])
print(st1[5:1]) # Space/Empty

# CASE 2. -ve BEGIN: -ve END
print(st1[-5:-2])
print(st1[-6: -1])
print(st1[-1:-5]) # Space/Empty

#CASE 3. +ve BEGIN: -ve END
print(st1[1:-1])
print(st1[2:-3])
print(st1[5:-2]) # Space/Empty

#CASE 4. -ve BEGIN: +ve END
print(st1[-6:4])
print(st1[-3:5])
print(st1[-4:4])
print(st1[-6:6])

