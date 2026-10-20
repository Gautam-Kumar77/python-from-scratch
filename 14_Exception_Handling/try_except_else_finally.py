#Ex1

try:
    a= float(input("Enter First Number:- "))
    b= float(input("Enter Second Number:- "))
    z= a/b
except ZeroDivisionError:
    print("Don't Enter Denominator as Zero")
except ValueError:
    print("Please Don't Enter String, AlphaNumeric and Special Character")
else:
    print("="*40)
    print("Devision is:- ", z)
    print("=" * 40)
finally:
    print("I am from Finally Block")

#Ex2
try:
    a1=float(input("Enter First Number:- "))
    b1=float(input("Enter Second Number:-"))
    c1= a1/b1
except (ZeroDivisionError, ValueError):
    print("Denominator can't be zero")
    print("Please Don't Enter String, AlphaNumeric and Special Character")
else:
    print("Div :- ", c1)
finally:
    print("This block is from finally")