try:
    fp= open("file.data", "r" )
except FileNotFoundError:
    print("File does not exist.")
else:
    print("File opened in read mode successfully...")
    print("Type of:-", type(fp))
finally:
    print("---------------------------------------------")
    print("I m from finally block")
    try:
        print("Is file closed before close()? :-", fp.closed)
        fp.close()
        print("Is file closed after close()? :-", fp.closed)
    except NameError:
        print("\tFILE ITSELF NOT OPENED-NO NEED TO CLOSE")
