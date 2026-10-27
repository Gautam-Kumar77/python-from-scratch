from module_for_UserDefinedException import SpaceError , EmptyNameError , InvalidNameError
def validation(name):
    if (name.isspace()):
        raise SpaceError
    else:
        words = name.split()
        if len(words)==0:
            raise EmptyNameError
        else:
            res= True
            for i in words:
                if(not i.isalpha()):
                    res= False
                    break
            if(res):
                return " ".join(words)
            else:
                raise InvalidNameError

try:
    nm= input("Enter Your Name:- ")
    res= validation(nm)
except SpaceError:
    print("Don't enter space")
except InvalidNameError:
    print("Dont enter symbols, alpnum and number... Try Again")
except EmptyNameError:
    print("Dont enter space only... Enter Your name")
else:
    print("Your Name:- {}".format(res))