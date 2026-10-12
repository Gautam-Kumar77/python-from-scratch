                                                    #filter()
                                                    #map()
                                                    #reduce()

#filter()

#Ex.1 Program for Filtering +VE Values from Given List of Values
def op(val):
    if val>0:
        return True
    else:
        return False
lst= [45,-43,-432,-2,45,90,-7]
vfil= filter(op, lst)
lstobj= list(vfil)
print(lstobj)

#Ex.2 Program for Filtering +VE Values from Given List of Values
def pos(val):
    return val>0
def neg(val):
    return val<0
print("Enter Values Seperated by Comma::- ")
lstobj= [float(val) for val in input().split(",")]
psval= list(filter( pos,lstobj))
ngval= tuple(filter(neg, lstobj))
print("Positive Value:- ", psval)
print("Negative Value:- ", ngval)

#Ex.3 Program for Filtering +VE Values and -VE value by using lambda function
pos= lambda val: val>0
neg= lambda val: val<0

print("Enter values by commas:- ")
opr= [float(val) for val in input().split(",")]
oprobj= list(filter(pos, opr))
oprob1= tuple(filter(neg, opr))
print("Positive Values:-", oprobj)
print("Negative values:- ", oprob1)

# Ex.4 Program for Filtering +VE Values and -VE value by using lambda function
print("Enter values seperated by comma:- ")
opr= [float(val) for val in input().split(",")]
pos= list(filter(lambda a: a>0, opr))
neg= tuple(filter(lambda b: b<0, opr))
print("Positive Number:", pos)
print("Negative Number:", neg)


#map()

#Ex1. program for accepting List of Salaries of Employees and Give 50 % Hike to Every Employee
def hike(sal):
    return sal+sal*50/100
#Main Program
oldsalary= [1000,1500,2000,40000]
res= list(map(hike, oldsalary))
for i,j in zip(oldsalary, res):
    print(i, "\t", j)

#Ex.2 #program for accepting List of Salaries of Employees and Give 50 % Hike to Every Employee