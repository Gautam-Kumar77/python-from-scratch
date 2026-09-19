#program for accepting and display Its Name
num= int(input("Enter a number: "))
if num==0:
    print("{} is Zero".format(num))
elif num==1:
    print("{} is One".format(num))
elif num==2:
    print("{} is Two".format(num))
elif num==3:
    print("{} is Three".format(num))
elif num==4:
    print("{} is four".format(num))
elif num==5:
    print("{} is five".format(num))
elif num==6:
    print("{} is six".format(num))
elif num==7:
    print("{} is seven".format(num))
elif num==8:
    print("{} is eight".format(num))
elif num==9:
    print("{} is nine".format(num))
elif num>9:
    print("{} is Positive Number:".format(num))
elif num in range(-1,-10,-1):
    print("{} is -VE digit".format(num))
else:
    print("{} is -VE number".format(num))
print("Program Execution Completed.")