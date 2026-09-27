                                        #BREAK

# Ex:1 Program for Demonstrating break keyword
# s= "PYTHON"
# for i in s:
#     if i=="H":
#         break
#     print(i)
#
# # Ex:2 Program for Demonstrating break keyword display Only PYTH without using Slicing and Indexing
# s= "PYTHON"
# i=0
# while(i<=len(s)):
#     if s[i]=="T":
#         break
#     print("{}".format(s[i]),end="")
#     i= i+1
#
# # Ex:3 Program for accepting a Numerical Integer Value and  Decide whether It  is Prime or not
# n= int(input("Enter a number: "))
# if n<=1:
#     print("Invalid Input!")
# else:
#     res= "PRIME"
#     for i in range(2, n):
#         if n%2==0:
#             res= "NOT PRIME"
#             break
#     print("\t{} is {}".format(n, res))
#
# # Ex:4 Program for accepting a Numerical Inetger Value and Decide whether It  is Prime or not
# n=int(input("Enter Any Integer Value:"))
# if(n<=1):
#     print("{} is Invalid Input".format(n))
# else:
#     res= False
#     for i in range(2, n):
#         if n%i==0:
#             res= True
#             break
#     if(res):
#         print("{} is NOT PRIME".format(n))
#     else:
#         print("{} is PRIME".format(n))
#
# # Ex5: Program for accepting any word and decide whether It is Vowel word or not
# n= input("Enter a character: ")
# word= "aeiouAEIOU"
# for i in word:
#     if n==i:
#         print("It is vowel")
#         break
# else:
#    print("Not vowel")

                                #CONTINUE

#Ex6: Program for Demonstrating continue keyword but want to display Only PYTON
# s= "PYTHON"
# for i in s:
#     if i=="H":
#         continue
#     print("{}".format(i), end="")
#

#Program for Reading List of Values and get and display +Ve values and -ve values
n= int(input("Enter how many numbers you want to store"))
if n<=0:
    print("Invalid Input!")
else:
    lst= list()
    for i in range(1, n+1):
        val= float(input("Enter number {}: ".format(i)))
        lst.append(val)
    else:
        print("List of Values=", lst)
        emptlist=[]
        for val in lst:
            if val<=0:
                continue
            emptlist.append(val)
        else:
            print("+ve values",emptlist)
            emplst= []
            for val in lst:
                if val>=0:
                    continue
                emplst.append(val)
            else:
                print("- ve values: ", emplst)
