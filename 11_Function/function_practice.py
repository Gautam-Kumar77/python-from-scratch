# #Ex1: Functions for Cal simple Interest
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