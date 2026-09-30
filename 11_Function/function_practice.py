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

#Ex2: program from adding the number take the input from user
def add(a,b):
    c= a+b
    return c
s= int(input("Enter a number:"))
s1= int(input("Enter a number:"))
print("({}, {}): {}".format(s,s1,add(s,s1)))

