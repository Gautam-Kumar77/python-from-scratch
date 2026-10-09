                                #Global and Local variable

# 1. Program for Demonstrating the Use of Local and Global Variables
def learnAI():
    a= 10
    print("This is local variable {} and this is global variable {}".format(a, c))
def learnAI1():
    b= 11
    print("This is local variable {} and this is global variable {}".format(b, c))

c= 20
learnAI()
learnAI1()

#2. Program for Demonstrating the Use of Local and Global Variables
lang= "Python"
def learnML():
    sub1= "ML"
    print("To use {} we use {} language.".format(sub1, lang))
def learnAI():
    sub2= "AI"
    print("To use {} we use {} language".format(sub2, lang))
learnML()
learnAI()

# 3. Program for Demonstrating the use of local and global variables
glb= 100
def lang1():
    global glb
    glb1 = glb+10
    return glb1
def mult():
    global glb
    glb2= glb*10
    return glb2

print("Global variable value before increment: ", glb)
glb1= lang1()
print("After Increment:- ", glb1)
glb2= mult()
print("After Multiply:- ",glb2)

#4. Program for Demonstrating Global Keyword
a=10
b=20
def increment():
    global a,b
    a= a+1
    b=b+1
def modify():
    global a,b
    a= a*2
    b= b*2
def accessvalues():
    c= a+2
    d= b+3
#Main Program
print("In Main Program: Global Variable values before increment(): a={} b={}".format(a,b)) # 10 20
increment()
print("In Main Program: Global Variable values after increment(): a={} b={}".format(a,b))
modify()
print("In main program: Global variable values after modify(): a={}, b={}".format(a,b))
accessvalues()
print("In main Program: Global variable values after accessvalue(): c={}, d={}".format(a,b))

#5. Program for Demonstrating globals()
#In this Program we have Unique Names for Global and Local Variables
a=100
b=200
c1=300
def operation():
    x= 1000
    y= 2000
    z= 3000
    res= a+b+c1+x+y+z
    print("Adding", res)
operation()

#6. Program for Demonstrating globals()
#In this Program we have SAME NAMES for Global and Local Variables
a1=200
b1= 400
def opr1():
    a1=100
    b1=300
    res= a1+b1+ globals() ["a1"] + globals() ["b1"]
    print(res)
opr1()

#Program for Demonstrating globals()
#In this Program we have SAME NAMES for Global and Local Variables
#GlobalsFunEx3.py
a=10
b=20 # Here a,b are Called Global Varaibles
def operation():
	k=globals()
	print("-"*50)
	print("Implicit and Programmer-Defined Global Variables")
	print("-"*50)
	for gvn,gvv in k.items():
		print("{}-->{}".format(gvn,gvv))
	print("-"*50)
	print("Programmer-Defined Global Variables--Way-1")
	print("-"*50)
	print("\tGlobal Var a={}".format(k.get('a')))
	print("\tGlobal Var b={}".format(k.get('b')))
	print("-"*50)
	print("Programmer-Defined Global Variables--Way-2")
	print("-"*50)
	print("\tGlobal Var a={}".format(k['a']))
	print("\tGlobal Var b={}".format(k['b']))
	print("-"*50)
	print("Programmer-Defined Global Variables--Way-3")
	print("-"*50)
	print("\tGlobal Var a={}".format(globals().get('a')))
	print("\tGlobal Var b={}".format(globals().get('b')))
	print("-"*50)
	print("Programmer-Defined Global Variables--Way-4")
	print("-"*50)
	print("\tGlobal Var a={}".format(globals()['a']))
	print("\tGlobal Var b={}".format(globals()['b']))
	print("-"*50)

#Main Program
operation()
