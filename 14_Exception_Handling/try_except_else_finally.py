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

