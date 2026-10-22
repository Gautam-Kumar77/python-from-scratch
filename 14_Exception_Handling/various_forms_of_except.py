#Form-1: Single except block ------> which can handle or process one exception at a time
#Ask the user to enter an integer. If they enter text such as 'hello' or 'abc', handle the error and print 'Invalid input'
try:
    n= int(input("Enter a number: "))
except ValueError:
    print("Invalid Input")
else:
    print(n)

#Form-2: Single except block with multiple exceptions
#Take two numbers as input and divide the first by the second. Handle invalid input and division by zero.
try:
    a= int(input("Enter a number: "))
    b= int(input("Enter second number: "))
    c=a/b
except (ZeroDivisionError, ValueError):
    print("Denominator can't be zero.")
    print("Please dont enter alphanumeric, string and symbol")
else:
    print("Division is", c)

#Form-3 :  single except block with alias name
