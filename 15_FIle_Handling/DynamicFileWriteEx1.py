def datawrite():
    print("Enter the data...(Press @ to stop)")
    with open("Testing1.txt", "a") as fp:
        while(True):
            fpdata= input()
            if fpdata != '@':
                fp.write(fpdata+"\t")
            else:
                print("Data written to the file...")
                break
datawrite()