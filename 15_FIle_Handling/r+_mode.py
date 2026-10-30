with open("Testing1.txt", "r+") as fp:
    print("File opened successfully in read mode")
    print("Readable:-", fp.readable())
    print("Writable:-", fp.writable())
    print("\tFile Name =", fp.name)
    print("\tFile Mode=", fp.mode)