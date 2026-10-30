#Ex1
name= "Gautam"
marks= 90
address= "Patna"
with open("file.data", "w") as fp:
    fp.write(name+"\t")
    fp.write(str(marks)+"\t")
    fp.write(address+"\t")
    print("Data Written to the File")

#Ex2
itrobj= {1:"Java", 2:"Python", 3:"Ruby"}
with open("D:\\Java\\Demo.txt", "a") as fpp:
    fpp.writelines(str(itrobj)+"\t")
