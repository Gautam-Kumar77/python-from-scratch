#Ex1: Functions for Cal simple Interest
def simpInt():
    p= int(input("Enter Principle: "))
    t= int(input("Enter Time: "))
    r= int(input("Enter rate: "))
    return p,t,r

def calculate(p,t,r):
    si= (p*r*t)/100
    totalamt= si+p
    return si, totalamt

def disp(si,totalamt):
    print("Simple Interest: ", si)
    print("Total Amount: ", totalamt)

#Main Program
a,b,c= simpInt()
si, totalamt= calculate(a,b,c)
disp(si,totalamt)


#Ex2: Functions for Cal simple Interest
def simpint():
    P = int(input("Enter Principle: "))
    T = int(input("Enter Time: "))
    R = int(input("Enter rate: "))
    return P,T,R

def calSimp():
    P,R,T= simpint()
    si= (P*R*T)/100
    totalamt= P+si
    return P,R,T,si,totalamt

def dispSimp():
    P,R,T,si,totalamt= calSimp()
    print("Simple Interest: ", si)
    print("Total Amount: ", totalamt)

dispSimp()

#Functions for Finding Length of words in a Line fo Text
s= input("Enter a sentence: ")
s1= s.split()
for i in s1:
    print( "{} : {}".format(i, len(i)))

#Using Function
def leng():
    return input("Enter a string: ")
def calc():
    lengt= leng()
    l= lengt.split()
    for i in l:
        print("{}:{}".format(i, len(i)))
calc()

#Functions for Generating Mul Table
def mul():
    n= int(input("Enter a number to print table: "))
    return  n
def calc():
    cal= mul()
    for i in range(1,11):
        print("{} * {} : {}".format(cal,i,cal*i))
calc()