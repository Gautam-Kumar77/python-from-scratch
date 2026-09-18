# #Ex 1. Write a Python program to check whether a person has a movie ticket using a simple if statement.
# # If the ticket is available, display messages for entering the theater, watching the movie, and understanding the message.
#
# tkt= input("Do you have a ticket(yes/no)?")
# if tkt.lower()=="yes":
#     print("\tWelcome to Theatre")
#     print("\tEnjoy Movie!")
# print("Go to Home")
#
# #program for accepting any value and Decide whether It is Palindrome or not
# val= input("Enter any Value: ")
# if val==val[::-1]:
#     print("{} is Palindrome".format(val))
# if val!=val[::-1]:
#     print("{} is not Palindrome".format(val))
# print("Program executed successfully")

#Program for accepting any Numerical value and Decide whether It is +VE or -VE or Zero
num= int(input("Enter any Numerical value: "))
if num>0:
    print("{} is +ve number".format(num))
if num<0:
    print("{} is -ve number".format(num))