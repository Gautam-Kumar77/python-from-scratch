def greet(name):
    print("Good Morning! \n\t\t {}".format(name))

#main Program
print("Type of Greet: ", type(greet))
greet("Gautam")

#Approach 1
#Function Def for Adding Two Numbers
# INPUT         : Input Taking From Function Call
# PROCESS       : Processing Done in Function Body
# OUTPUT        : Output Returned to Function Call

def addtwo(a,b):
    c= a+b
    return c

r= addtwo(3,6)
print("Sum:= ", r)
t= addtwo(67,54)
print("Sum: ", t)

# #Ex2: program from adding the number take the input from user
def add(a,b):
    c= a+b
    return c
s= int(input("Enter a number:"))
s1= int(input("Enter a number:"))
print("({}, {}): {}".format(s,s1,add(s,s1)))

#Approach 2
# INPUT         : Input Taking Inside of Function Body
# PROCESS       : Processing Done in Function Body
# OUTPUT        : Output Displayed in Function Body

#Function Def for Adding Two Numbers
def sub():
    a= int(input("Enter a number: "))
    b= int(input("Enter 2nd number: "))
    c= a-b
    print("Subtraction is: ",c)
sub()


#Approach 3
# INPUT         : Input Taking From Function Call
# PROCESS       : Processing Done in Function Body
# OUTPUT        : Output Displayed in Function Body
#Function Def for Adding Two Numbers
def addtwo(a,b):
    c=a+b
    print( "({} + {}) = {}".format(a,b,c))

a=int(input("Enter first Number: "))
b=int(input("Enter second number: "))
addtwo(a,b)


#Approach 4
# INPUT         : Input Taking Inside of Function Body
# PROCESS       : Processing Done in Function Body
# OUTPUT        : Output Returned to Function Call

# Function Def for Adding Two Numbers
def sumop():
    a= int(input("Enter a number: "))
    b= int(input("Enter second number: "))
    c= a+b
    return a,b,c
x,y,z= sumop()
print("sum({},{})= {}".format(x,y,z))
