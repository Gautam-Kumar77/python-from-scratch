#Ex1: program for Reading the Data from any File---read()
try:
    with open("file.data", "r") as fr:
        filename= fr.read()
        print(filename)
except FileNotFoundError:
    print("File does not exist")

#Ex2: program for Reading the Data from any File---readlines()

try:
    with open("Testing1.txt", "r") as fr1:
        filename1 = fr1.readlines()
        print("------------------------------------------")
        print(filename1)
        print("------------------------------------------")
except FileNotFoundError:
    print("File does not exist")

#Ex3: Program for Reading the Content of Any File using function
def dispfile():
    n= input("Enter any file name:")

    try:
        with open(n, "r") as fn1:
            filename2= fn1.read()
            print("--------------------------")
            print(filename2)
            print("--------------------------")
    except FileNotFoundError:
        print("File does not exist")

dispfile()