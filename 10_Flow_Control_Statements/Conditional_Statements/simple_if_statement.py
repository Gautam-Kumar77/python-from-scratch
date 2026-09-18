#Ex 1. Write a Python program to check whether a person has a movie ticket using a simple if statement.
# If the ticket is available, display messages for entering the theater, watching the movie, and understanding the message.

tkt= input("Do you have a ticket(yes/no)?")
if tkt.lower()=="yes":
    print("\tWelcome to Theatre")
    print("\tEnjoy Movie!")
print("Go to Home")