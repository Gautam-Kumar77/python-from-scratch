#Positional Argument
def disstddata(name, roll, course):
    print("\t{} \t{} \t{}".format(name,roll,course))

print("\tName \tRoll \tCourse")
print("_"*40)
disstddata("Rahul", 102, "btech")
disstddata("Rohan", 103, "BBA")
disstddata("Rohini",342, "BCA")

#Program for Demonstrating Positional Arguments
def stdtl(name, phone, address):
    print("\t{} \t{} \t{}".format(name,phone,address))

print("\tName \tPhone \t\tAddress")
print("-"*40)
stdtl("Sarvan", 897634587, "Muzaffarpur")
stdtl(address="Sheohar", name="Ramesh", phone=6787908765)
# stdtl(phone=892839289, name="Shyam", "Patna") SyntaxError: positional argument follows keyword argument

#Keyword arguments
def keyarg(a,b,c,d):
    print("\t{} \t{} \t{} \t{}".format(a,b,c,d))
keyarg(a=23,b=45,c=43,d=34)
keyarg(12, b=45,c=89,d= 34)
keyarg(100, c=90, d=97, b=89)
# keyarg(91, c=89, d= 90)   TypeError: keyarg() missing 1 required positional argument: 'b'


#Default arguments
def dfltarg(name,course, city="HYD", country= "India"):
    print("{}\t {}\t {}\t  {}\t ".format(name, course, city, country))
dfltarg('A', "MBA")
dfltarg('A', "MBA", city="Delhi")
dfltarg(country="Algeria", name="Rahul", city="BNG", course="LLB")


#Variable length argument
#Program for Demonstrating the Concept of Variable Length Arguments
def valeng(*arg):
    print(arg, type(arg), len(arg))
valeng(10)
valeng(10,30)
valeng(10,20,30)
valeng()


# Program for Demonstrating the Concept of Variable Length Arguments
# PureVariableLengthArgsEx2.py
def disp(*kv):
    for i in kv:
        print(i, end=" ")
    print()
disp(10,20,30,40)
disp(10,20,30)
disp(10,20)

#Program for Demonstrating the Concept of Variable Length Arguments
def varlen(sno,name,marks,*vals):
    print("Student Number:- ",sno)
    print("Student Name:- ", name)
    print("Students marks:- ",marks)
    print("Variable length values {}\n sum= {}".format(vals, sum(vals)))
    print("-"*50)
varlen(12,"Sanchit", 90, 10,20,30,40)
varlen(3, "Rajesh", 89, 20,40, 60)
varlen(12, "Ramesh", 4, 67,57,65)