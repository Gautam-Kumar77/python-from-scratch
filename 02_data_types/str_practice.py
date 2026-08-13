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

#This Syntax Generates Range of Characters OR Sub String from BEGIN Index to END-1 Index in FORWARD Direction with
# Default Step +1  provided  BEGIN < END Index Otherwise we get Space OR ' ' as Result.

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
#In this Syntax, We are Specifying the BEGIN Index and Not Specifying END Index.

#strObj[BEGIN: ]
s= "PYTHON"
print(s[2:])
print(s[0:])
print(s[0:1000])
print(s[-2:])
print(s[-5:])
print(s[-1000:])

                                             #Syntax 3
#In this Syntax, We are Specfying the END Index and Not Specifying  BEGIN Index.

#strObj[ :END]
print(s[: 4])
print(s[:100])
print(s[:-2])
print(s[: -4])

                                            #Syntax 4
#In this Syntax, We are Not Specfying Both BEGIN and  END Indices

#strObj[:]
print(s[:])
addr= "Hyderabad"
print(addr[:])

                                            #Syntax 5
#
#strObj[BEGIN:END:STEP]

#Rule 2. If the Value of STEP is +VE then PVM Takes of Range of Chars from BEGIN Index to END-1 Index in FORWARD
        #Direction  by Maintaining the Value of STEP provided BEGIN < END Otherwise we get Sapce(' ') as Result

# +ve BEGIN: +ve END : +ve STEP
print(s[1:6:1])
print(s[0:5:2])
print(s[1:6:1])
print(s[0:6:4])

# -ve BEGIN: -ve END : +ve STEP
print(s[-6:-1:1])
print(s[-5:-2:2])
print(s[-2:-4:3])  #Empty/Space

#  +ve BEGIN: -ve END : +ve STEP
print(s[1:-1:2])
print(s[2:-2:2])
print(s[3:-3:3])   #Empty/Space

# -ve BEGIN: +ve END : +ve STEP
print(s[-6:6:1])
print(s[-5:5:3])
print(s[-100:100:4])

#Rule 3. If the Value of STEP is -VE then PVM Takes Range of Chars in BACKWARD Direction  from BEGIN Index to END+1
         #Index by Maintaining the Value of STEP Provided BEGIN > END Index Otherwise we get Sapce(' ') as Result.

# +ve BEGIN: +ve END : -ve STEP
print(s[5:0:-1])
print(s[5:2:-2])
print(s[4:1:-3])

#-ve BEGIN: -ve END : -ve STEP
print(s[-1:-7:-1])
print(s[-2:-7:-3])
print(s[-2:-100:-2])

#+ve BEGIN: -ve END : -ve STEP
print(s[4:-6:-2])
print(s[100:-100:-1])
print(s[5:-4:-2])

#-ve BEGIN: +ve END : -ve STEP
print(s[-1:2:-1])
print(s[-2:2:-2])
print(s[-4:0:-1])

#We can Reverse a string by using extended slicing concept
hyd= "HYDERABAD"
print(hyd[-1:-10:-1])

py= "PYTHON"
print(py[-1:-100:-1])
print(py[100:-100:-1])

#We can also find Palindrome by using extended slicing concept
m= "MADAM"
print(m[-1:-6:-1])
n= "NAMAN"
print(n[100:-100:-1])

#Rule 4 When we extract the data in forward direction, if we specify END INDEX 0 then we will get ''(empty/space)
print(s[5:0:1])
print(s[3:0:1])

#Rule 5 When we extract the data in backward direction, if we specify END INDEX -1 then we will get ''(empty/space)
print(s[2:-1:-1])
print(s[5:-1:-2])