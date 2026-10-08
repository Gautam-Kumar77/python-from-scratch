# #1. Positional Argument
# def disstddata(name, roll, course):
#     print("\t{} \t{} \t{}".format(name,roll,course))
#
# print("\tName \tRoll \tCourse")
# print("_"*40)
# disstddata("Rahul", 102, "btech")
# disstddata("Rohan", 103, "BBA")
# disstddata("Rohini",342, "BCA")
#
# #Program for Demonstrating Positional Arguments
# def stdtl(name, phone, address):
#     print("\t{} \t{} \t{}".format(name,phone,address))
#
# print("\tName \tPhone \t\tAddress")
# print("-"*40)
# stdtl("Sarvan", 897634587, "Muzaffarpur")
# stdtl(address="Sheohar", name="Ramesh", phone=6787908765)
# # stdtl(phone=892839289, name="Shyam", "Patna") SyntaxError: positional argument follows keyword argument
#
# #2. Keyword arguments
# def keyarg(a,b,c,d):
#     print("\t{} \t{} \t{} \t{}".format(a,b,c,d))
# keyarg(a=23,b=45,c=43,d=34)
# keyarg(12, b=45,c=89,d= 34)
# keyarg(100, c=90, d=97, b=89)
# # keyarg(91, c=89, d= 90)   TypeError: keyarg() missing 1 required positional argument: 'b'
#
# #3. Default arguments
# def dfltarg(name,course, city="HYD", country= "India"):
#     print("{}\t {}\t {}\t  {}\t ".format(name, course, city, country))
# dfltarg('A', "MBA")
# dfltarg('A', "MBA", city="Delhi")
# dfltarg(country="Algeria", name="Rahul", city="BNG", course="LLB")
#
#
# #4. Variable length argument
# #Program for Demonstrating the Concept of Variable Length Arguments
# def valeng(*arg):
#     print(arg, type(arg), len(arg))
# valeng(10)
# valeng(10,30)
# valeng(10,20,30)
# valeng()
#
#
# # Program for Demonstrating the Concept of Variable Length Arguments
# # PureVariableLengthArgsEx2.py
# def disp(*kv):
#     for i in kv:
#         print(i, end=" ")
#     print()
# disp(10,20,30,40)
# disp(10,20,30)
# disp(10,20)
#
# #Program for Demonstrating the Concept of Variable Length Arguments
# def varlen(sno,name,marks,*vals):
#     print("Student Number:- ",sno)
#     print("Student Name:- ", name)
#     print("Students marks:- ",marks)
#     print("Variable length values {}\n sum= {}".format(vals, sum(vals)))
#     print("-"*50)
# varlen(12,"Sanchit", 90, 10,20,30,40)
# varlen(3, "Rajesh", 89, 20,40, 60)
# varlen(12, "Ramesh", 4, 67,57,65)
#
# #5. Pure KeyWord Variables Length Parameters (or) arguments
#
# #Program for Demonstrating the Need of  Keyword Variable Length Arguments
# def disp( **kvr):
#     print(kvr,type(kvr),len(kvr))
# #Main Program
# disp(sno=10,sname="RS",mm=56,em=70,cname="PSF") # Function Call-1 with 5 Keyword  Variable length Arguments
# disp(tno=100,tname="TR",sub1="PYTHON",sub2="Numpy")# Function Call-2 with 4 Keyword Variable length  Arguments
# disp(cid=1000,cname="JH",hb="Drawing") # Function Call-3 with 3 Keyword  Variable length Arguments
# disp(a=10,b=20) # Function Call-4 with 2 Keyword Variable length  Arguments
# disp(k=30) # Function Call-5 with 1 Keyword Variable length  Arguments
# disp() # Function Call-6 with 0 Keyword Variable length Arguments"""


#Global and Local variable

#1. Program for Demonstrating the Use of Local and Global Variables
# LocalGlobalVarEx3.py

#Program for Demonstrating the Use of Local and Global Variables
def learnAI():
    a= 10
    print("This is local variable {} and this is global variable {}".format(a,c))
def learnAI1():
    b= 11
    print("This is local variable {} and this is global variable {}".format(b,c))

learnAI()
c= 20
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

#3. Program for Demonstrating the use of local and global variables
