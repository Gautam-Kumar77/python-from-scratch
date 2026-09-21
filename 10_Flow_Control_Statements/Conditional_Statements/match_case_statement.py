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

#program for Cal area of Different Figures by using match case
print("Program for calculating area of different figures: ")
print("="*50)
print("\t\t C. Circle")
print("\t\t R. Rectangle")
print("\t\t T. Triangle")
print("\t\t S. Square")
print("\t\t E. Exit")
print("="*50)

ch= input("Choose any one Operation: ")
match ch:
    case "C" | "c":
        a= float(input("Enter Radius"))
        if a<=0:
            print("Invalid Input")
        else:
            print("Area of Circle is {}".format(3.14 * a ** 2))

    case "R" | "r":
        a,b = float(input("Enter Breadth")), float(input("Height"))
        if a<=0 and b<=0:
            print("Invalid Input")
        else:
            print("Area of Rectangle is {}".format(a*b))

    case "T" | 't':
        b,h = float(input("Enter Breadth")) , float(input("Enter Height"))
        if b<=0 and h<=0:
            print("Invalid Input")
        else:
            print("Area of Triangle is {}".format(0.5*b*h))

    case 'S'|'s':
        side= float(input("Enter side"))
        if side<=0:
            print("Invalid Input")
        else:
            print("Area of square is {}".format(side*side))

    case "E"| 'e':
        print("Successfully exited")
        exit()
    case _:
        print("Please choose valid option")
