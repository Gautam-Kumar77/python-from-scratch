# # Q1
#
# a= int(input("Enter 1st Number"))
# b= int(input("Enter 2nd Number"))
# sum = a+b
# print("Sum is:-",sum)
#
#
# a= float(input("Enter a number:- "))
# z= float(input("Enter number from u want to divide"))
# rem= a%z
# print("Remainder is:- ", rem)
#
# # Q3
# a= int()
# b= float(3.0)
# c= str()
# d= bool(False)
# e= complex()
# print(a,type(a))
# print(b,type(b))
# print(c,type(c))
# print(d,type(d))
# print(e,type(e))
#
# a= input("Enter a number")
# print(type(a))
#
# a= 34
# b= 80
# opr= a>b
# print(opr)
#
# a= int(input("Enter 1st Number"))
# b= int(input("Enter 2nd Number"))
# c= int(input("Enter 1st Number"))
#
# avg = (a+b+c)/3
# print("Average:- ", avg)
#
# a= int(input("Enter a Number for square"))
# b= a*a
# print("Square is: ",b)
#
#                                     # String
#
# a=10
# b=6
# a,b = b,a
# print("Value of a:", a , "Value of B: ", b)
#
# i = 'Hello Gautam'
#
#
# print(i.startswith('He'))
# print(i.endswith('lo'))
# print(i.replace('Gautam', 'Python') )
# print(i.find('a'))
# print(i.count('a'))
#
# n= input("Enter Your Name: ")
# print("Good Evening", n)
#
# letter= input("Enter Your Name:")
# let= (input('Enter Date: '))
#
# print( f'''Dear {letter},
#        You are selected!
#        {let}''')
#
# let= 'Good   Morning'
# print(len(let[4:7]))
# print(let.replace("   ", " "))
#
#                                               # LIST(Mutable)
#
# li = ["Orange", 3 , 34.4, True, "Mango"]
# g=li.append("Potato")
# print(li)
#
# print(li[-1])
#
# demo= [3, "Orange", True, 88.3, "Morning"]
# # demo.insert(1, 'Potato')
# print(demo)
# # demo.remove("Morning")
# #demo.pop(1)
# #demo.clear()
# # print(demo.index(88.3))
# print(demo)
#
#                                             # TUPLE(Immutable)
#
# a1= (3,32, "G", False, 23.3)
# print(len(a1))
# # a1[1]=0
# print(a1.count(32))
# print(a1.index(32))
# print(32 in a1)
# b= (12,34,3)
# con= a1+b
# print(con)
# b= (12,) # If we want to store value give one comma(,) otherwise it will return int
# print(type(b))
# bv= 34,343 , "Game", True
# print(bv, type(bv))
#
# c= ([1,2], [3,4])
# c[0].append(5)
# print(c)
#
# num= list[input("Enter Seven Fruits name")]
# print(num)
#
# num1= list(input("Enter the marks of 6 students:"))
# num1.sort()
# print(num1)
#
# x = 10
# x += 5
# x *= 2
# x //= 3
# print(x)
#
# num1= int(input("Enter a number: "))
# print("Pass:",(num1>=40))
# print("Excellent: ", (num1>=80))
#
# # Addition
# # Subtraction
# # Multiplication
# # Division
# # Floor Division
# # Remainder
# # Power
#
# a= int(input("Enter first number: "))
# b= int(input("Enter second Number: "))
#
# print("Addition:- ", a+b)
# print("Subtraction:- ", a-b)
# print("Multiplication :- ", a*b)
# print("Division:- ", a/b)
# print("Floor Division:- ", a//b)
# print("Remainder:- ", a%b)
# print("Power:- ", a*a)
#
#
#
# # Q10
# #
# # Write a program that:
# #
# # Takes 5 numbers from the user.
# # Stores them in a list.
# # Prints the list.
# # Prints the sorted list.
#
# demo= []
# num= int(input("Enter First Number"))
# demo.append(num)
# num1= int(input("Enter second Number: "))
# demo.append(num1)
# num2= int(input("Enter Third number: "))
# demo.append(num2)
# num3= int(input("Enter fourth Number: "))
# demo.append(num3)
# num4= int(input("Enter fourth Number: "))
# demo.append(num4)
#
# print(demo.sort())
# print(demo)
#
# numbers = [10, 20, 30, 40, 50]
#
# print(numbers[::-1])
#
# numbers = [45, 12, 78, 23, 9, 56]
# print(max(numbers))
# print(min(numbers))
#
# numbers = [10, 20, 10, 30, 10, 40, 20]
# x= numbers.count(10)
# print(f" 10 occurs {x} times ")
#
# numbers = [10, 20, 30, 40, 50]
# numbers.append(60)
# numbers.remove(20)
# numbers[2]= 30
# numbers.reverse()
# print(numbers)
#                                    # DICTIONARY(Mutable)
#
# marks = {
#     "Suresh": 123,
#     "Ramesh" : 124,
#     "Rajesh": 90
# }
# # print(marks["Suresh"])
# print(marks.get("Suresh"))
# print(marks.keys())
# print(marks.values())
# print(type(marks))
# s1=marks.update({"Ramesh": 150, "Rajendra":12})
# marks["Suresh"]= 2
# print(marks.pop("Rajendra"))
#
# print(marks.clear())
#             #NOTE
# print(marks.get("city"))     # None
# print(marks["city"])            # KeyError
# print(marks)
#
# # Write a program that takes 5 student names and marks from the user and stores them in a dictionary.
#
# marks= {}
# m1= input("Enter 1st Name: ")
# m2= int(input("Enter marks: "))
# marks.update({m1:m2})
from nturl2path import pathname2url

# m2= input("Enter 2nd Name: ")
# m3= int(input("Enter marks: "))
# marks[m2]=m3
#
# print(marks)
# marks = {
#     "Gautam": 85,
#     "Rahul": 72,
#     "Aman": 90,
#     "Rohit": 65
# }
# for key, value in  marks.items():
#     print(key, value)
# student = {
#     "name": "Gautam",
#     "age": 22,
#     "course": "MCA"
# }
# print(student.keys())
# print(student.values())
# print(student.get("city"))
#
# addr={
#     "Name": "Gautam",
#     "Age" : 23,
#     "Course" : "MCA",
#     "Marks": 234
# }
# addr["city"]= "Hyd"
# addr.pop("Age")
# print(addr.keys(),  addr.values())

                                        #SET
#
# s= {3,4,5,6,6}
# su= {2,3,6,7}
# s1={} #<class 'dict'>
# s2= set() #<class 'set'>
# print(s, type(s))
# print(s1, type(s1))
# print(s2, type(s2))
# s.add(9)
# print(s.union(su))
# print(s.intersection(su))
# s.remove(6)
# print(s)
# print(len(s))

# Q1
# d= {
#     "Angoor": "Grapes",
#     "Kursi": "Chair",
#     "Pankha": "Fan"
# }
# for key , value in d.items():
#     print(key,":", value)
#
# s= set()
# n= int(input("Enter a number: "))
# s.add(n)
# n1= int(input("Enter a number: "))
# s.add(n1)
# n2= int(input("Enter a number: "))
# s.add(n2)
# n3= int(input("Enter a number: "))
# s.add(n3)
# n4= int(input("Enter a number: "))
# s.add(n4)
# n5= int(input("Enter a number: "))
# s.add(n5)
# n6= int(input("Enter a number: "))
# s.add(n6)
# print(s)
#
# s9= {18, "18"}
# print(s9)
#
# sw= set()
# sw.add(12)
# # sw.add(12.0)
# sw.add("12")
# print(len(sw))


# students= { }
# name= input("Enter Your Name: ")
# lan= input("Enter Your Fav Lang: ")
# students.update({name:lan})
# name1= input("Enter Your Name: ")
# lan1= input("Enter Your Fav Lang: ")
# students.update({name1:lan1})
# name2= input("Enter Your Name: ")
# lan2= input("Enter Your Fav Lang: ")
# students.update({name2:lan2})
# print(students)

                                        #Conditional Expression
# age= int(input("Enter Your Age:- "))
#
# if age>0 and age<=17:
#     print("You are teenager")
# elif age>=18 and age<60:
#     print("You are eligible to give vote ")
# elif age<0:
#     print("Bencho sahi age daal")
# else:
#     print("You are not eligible to give vote ")
# print("Program Terminated")

#WAP to find greatest of four numbers entered by user
# n1= int(input("Enter first number"))
# n2= int(input("Enter 2nd number"))
# n3= int(input("Enter 3rd number"))
# n4= int(input("Enter 4th number"))
#
# if n1>n2:
#     print(f"{n1} is greatest number:")
# elif n2>n3 and n2>n1:
#     print(f"{n2} is greatest number:")
# elif n3>n4 and n3>n2:
#     print(f"{n3} is greatest number:")
# else:
#     print(f"{n4} is greatest number:")

# sub1= int(input("Enter marks of English: "))
# sub2= int(input("Enter marks of Sanskrit: "))
# sub3= int(input("Enter marks of Computer: "))
#
# total= ((sub1+sub2+sub3)/300)*100
#
# if total>=40 and sub1>33 and sub2>33 and sub3>33:
#     print("Pass")
# else:
#     print("You are fail")

# p1= "Make a money"
# p2= "Buy new"
# p3="Subscribe this"
# p4="click this"
#
# message= input("Enter Your Comment: ")
# if (p1 in message) or (p2 in message) or (p3 in message) or (p4 in message):
#     print("This is Spam")
# else:
#     print("Nothing")
#
# n= input("Enter a number")
# if len(n)<10:
#     print("It contains less than 10 characters")
#
# else:
#     print("It contains more than 10 characters")

# l= ["Sourabh", "ram", "shyam"]
#
# t = input("Enter name to find: ")
# if t in l:
#     print("Name is present in list")
# else:
#     print("Name is not present in list")

s = "Harry is a good boy"
if "Harry" in s:
    print("Yes it is there")
else:
    print("Not there")