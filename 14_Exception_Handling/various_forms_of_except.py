#Form-1: Single except block ------> which can handle or process one exception at a time
#Ask the user to enter an integer. If they enter text such as 'hello' or 'abc', handle the error and print 'Invalid input'
try:
    n= int(input("Enter a number: "))
except ValueError:
    print("Invalid Input")
else:
    print(n)

# #Form-2: Single except block with multiple exceptions
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

#Form-3: single except block with alias name
#Create a list of five numbers. Ask the user for an index and print the value at that index. Handle invalid indexes and non-integer input.
numbers= [10,20,30,40,50]
try:
    n= int(input("Enter a number:- "))
    print("Value", numbers[n])
except ValueError as v:
    print("Invalid Input! Please Enter Integer Value", v)
except IndexError as i:
    print("Invalid Index! Please Enter between 1-4",i)

#Form-4: default
#Create a dictionary of three students and their marks. Ask for a student's name and print their marks. Handle a missing key.
dic = {
    "Rajan":12,
    "Ram":90,
    "Shyam" : 28
}
try:
    n=input("Enter Student name:- ")
    print("Marks of {} is {}".format(n,  dic[n]))
except:
    print("Something went wrong")

#Form-5: Recommended form --all the times
try:
    print("Program Execution Started")
    a=input("\tEnter First Value:")
    b=input("\tEnter Second Value:")
    x=float(a)   #  exception stmt------ ValueError
    y=float(b)  #  exception stmt------ ValueError
    z=x/y   #  exception stmt------ ZeroDivisionError
    s="PYTHON"
    print(s[10])  # IndexError
except ZeroDivisionError:
    print("\tDON'T ENTER ZERO FOR DEN....")
except ValueError:
    print("\tDON'T ENTER ALNUMS,STRS AND SYMBOLS")
except IndexError:
    print("\tCheck Ur Index")
except: #Default  except block---for Handling UnKnown Future Exceptions
    print("\tOooooooops  Some thing went wrong..try again")
else:
    print("----------------------------------------------")
    print("\tFirst Value=",x)
    print("\tSecond Value=",y)
    print("\tDiv=",z)
    print("Program Execution Ended")
    print("----------------------------------------------")
finally:
    print("I am from finally Block")