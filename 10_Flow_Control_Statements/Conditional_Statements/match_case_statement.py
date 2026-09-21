#program for Implementing Arithmetic Operations By using Match Case
print("Perform Arithmetic Operation")
print("="*40)
print("\t\t 1.Addition")
print("\t\t 2.Subtraction")
print("\t\t 3.Multiplication")
print("\t\t 4.Division")
print("\t\t 5.Floor Division")
print("\t\t 6.Modulo Division")
print("\t\t 7.Exponentiation")
print("="*40)

ch= int(input("Choose any one operation:- "))
match ch:
    case 1:
        print("Enter two numbers for addition")
        a= float(input("Enter a number: "))
        b= float(input("Enter second number: "))
        print("Addition of {} and {} = {}".format(a,b,a+b))

    case 2:
        print("Enter two numbers for Subtraction")
        a = float(input("Enter a number: "))
        b = float(input("Enter second number: "))
        print("Addition of {} and {} = {}".format(a, b, a-b))

    case 3:
        print("Enter two numbers for Multiplication: ")
        a= float(input("Enter First Number"))
        b= float(input("Enter Second Number"))
        print("{}*{} = {}".format(a,b,a*b))

    case 4:
        print("Enter two number for Division: ")
        a= float(input("Enter first Number "))
        b= float(input("Enter second Number "))
        print("{}/{} = {}".format(a,b,a/b))

    case 5:
        print("Enter two number for floor Division:")
        a,b= int(input("Enter first number")), int(input("Enter Second Number"))
        print("{}//{}= {}".format(a,b,a//b))

    case 6:
        print("Enter Two numbers for modulo division")
        a, b = int(input("Enter first number")), int(input("Enter Second Number"))
        print("{}%{}= {}".format(a, b, a % b))

    case 7:
        print("Enter two numbers for exponentiation: ")
        a, b = int(input("Enter first number")), int(input("Enter Second Number"))
        print("{} ** {} = {}".format(a,b,a**b))
    case _ :
        print("Please choose valid option")

print("Program Executed Successfully..")
