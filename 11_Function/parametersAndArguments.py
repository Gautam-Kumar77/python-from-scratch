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
