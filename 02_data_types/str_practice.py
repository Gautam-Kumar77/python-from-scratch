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
                                             #Syntax 1
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

                                                      #SYNTAX 2

#strObj[BEGIN: ]
s= "PYTHON"
print(s[2:])
print(s[0:])
print(s[0:1000])
print(s[-2:])
print(s[-5:])
print(s[-1000:])

                                             #Syntax 3

#strObj[ :END]
print(s[: 4])
print(s[:100])
print(s[:-2])
print(s[: -4])

                                            #Syntax 4

#strObj[:]
print(s[:])
addr= "Hyderabad"
print(addr[:])

                                            #Syntax 5
#strObj[BEGIN:END:STEP]

#Rule 1. +ve BEGIN: +ve END : +ve STEP
print(s[1:6:1])
print(s[0:5:2])
print(s[1:6:1])
print(s[0:6:4])

#Rule 2. -ve BEGIN: -ve END : +ve STEP
print(s[-6:-1:1])
print(s[-5:-2:2])
print(s[-2:-4:3])  #Empty/Space

#Rule 3. +ve BEGIN: -ve END : +ve STEP
print(s[1:-1:2])
print(s[2:-2:2])
print(s[3:-3:3])   #Empty/Space

#Rule 4. -ve BEGIN: +ve END : +ve STEP
print(s[-6:6:1])
print(s[-5:5:3])
print(s[-100:100:4])