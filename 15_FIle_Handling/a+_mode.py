with open("Sample.data","a+") as fp:
    print("-------------------------------------------------")
    print("File Opened Successfully in Write Mode")
    print("\tType of fp=",type(fp))
    print("\tIs File Closed within with open() as Ind: ",fp.closed) # False
    print("\tFile Name =",fp.name)
    print("\tFile Mode=",fp.mode)
    print("\tIs File Readable=",fp.readable())# True
    print("\tIs File Writable=",fp.writable())# True
    print("-------------------------------------------------")
print("Is File Closed after comes out-off with open() as Ind: ",fp.closed) # False


with open("D:\\Java\\Demo.txt", "x+") as tp:
    print("File opened successfully")