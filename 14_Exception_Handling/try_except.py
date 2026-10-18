try:
    a= input("Enter First value:- ")
    b= input("Enter Second value:- ")
    x= float(a)
    y= float(b)
    c=x/y
except ZeroDivisionError:
    print("Dont enter zero in denomenator")
except ValueError:
    print("Don't enter syntax, alnum and str")
else:
    print("*"*30)
    print("First Value {}".format(x))
    print("Second Value {}".format(y))
    print("Division is: ", c)
