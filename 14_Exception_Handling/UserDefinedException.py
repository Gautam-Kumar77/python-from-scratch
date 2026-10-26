from module_for_UserDefinedException import InvalidAgeError
from module_for_UserDefinedException import NumberDevisionError
from module_for_UserDefinedException import ZeroError , NegativeNumberError
from builtins import ValueError

#Ex1
try:
    n= int(input("Enter Your Age: "))
    if n<=18:
        raise InvalidAgeError("You Cant Vote, Age must be Greater than or equal to 18")
except InvalidAgeError as i:
    print("Error:", i)
else:
    print("You are Eligible")

#Ex2:
def div(a,b):
    if b==0:
        raise NumberDevisionError
    else:
        return a/b

try:
    a= int(input("Enter first number: "))
    b= int(input("Enter Second Number: "))
    c= div(a,b)
except NumberDevisionError:
    print("Denominator cant be zero")
except ValueError:
    print("Dont enter alnum, string and symbol")
else:
    print("Division is: {}".format(c))

#Ex3:

def table(n):
    if n==0:
        raise ZeroError
    elif n<0:
        raise NegativeNumberError
    else:
         for i in range(1,11):
             print(n, "*", i ,"=", n*i)
try:
    n= int(input("Enter a number for printing table:- "))
    table(n)
except ZeroError:
    print("Dont Enter Zero for mul table")
except ValueError:
    print("Please Dont enter string, alpnum and symbol")
