#Ex.1 Program for Finding Length of Each word Present list by using Dict Comprehension
lst = ["apple", "Banana", "Mango"]
d= {val: len(val) for val in lst}
print(d, type(d))

#Ex.2 Program for Finding Squares of Numerical +VE Values by using Dict Comprehension
lst1= [2,4,7,3,-2]
dt= {val: val**2 for val in lst1 if val>0}
pt= {val: val**2 for val in lst1 if val<0}
print(dt)
print(pt)

#Ex.3 Program for Getting all Even Numbers By using List Comprehension
lst2= [109,46,44,23,13,78,90,76,45]
evn= {d for d in lst2 if d%2==0}
od= {d for d in lst2 if d%2!=0 }
print("Even Numbers:",evn)
print("Odd numbers:", od)

#Ex.4 program for Reading the values from Key Board By using List Comprehension
print("Enter List of Numerical Values Separated by Comma:")
lst= [float(val) for val in input().split(",")]
print("List of values: ", lst)