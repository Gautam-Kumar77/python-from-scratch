fp= open("file.data", "w")
print("File created and opened in write mode successfully.")
print("Type of fp:- ", type(fp))

try:
    with open("Testing1.txt", "w") as fpp:
        print("File Opened Successfully in read mode")
        print('type of fpp', type(fpp))
        print("Is File Closed within open(): ?", fpp.closed)
        print("Name:-", fpp.name)
        print("Mode:-", fpp.mode)
    print("Is file closed:", fpp.closed)
except FileNotFoundError:
    print("File doesnt exist...")
