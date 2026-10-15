BNAME= 'icici'
ADDR= "Delhi"

def simpInt():
    p= int(input("Enter Principle:-"))
    r= int(input("Enter Rate:-"))
    t= int(input("Enter tine:-"))
    si = (p*r*t)/100
    return p,r,t,si
def new():
    p,r,t,si= simpInt()
    print("Principle:-", p)
    print("Rate:-",r)
    print("Time:- ",t)
    print("Interest is:-",si)
    print("Total Amount is:-", p+si)
