                                        #and operator
print("Using and Operator\n")
#eg1
print(True and False)
print(False and True)
print(False and False)
print(True and True)

#eg2
print(12>34 and 342>23)
print(90>20 and 100>90 and 40>23)
print(20>10 and 100>190 and 40>23)
print(900>100 and 100>90 and 140>230)

#eg3: Special
print(100 and 200)
print(-200 and -300)
print(0 and 200)
print(100 and 0)
print(100 and 20 and True)
print("Java" and "Python")
print("Java" and "Python" and " ")

                                        # or operator
#eg1
print("Using or Operator\n")
print(True or False)
print(False or True)
print(False or False)
print(True or True)

#eg2
print(10>2 or 34>12)
print(10>20 or 34>102)
print(10>201 or 34>12 or 50>34)
print(80>100 or 20>102 or 45>200 )

#eg3: special
print(100 or 200)
print(200 or 100)
print(100 or 0)
print(0 or 100)
print(0 or 200 or 900)
print("Java" or "Python")
print("Java" or "Python" or " ")

                                        #not operator

#eg1
print(not(True))
print(not(False))
print(not(10>20 and 90>10))

#eg2
print(bool(10))
print(not(bool(10)))
print(100 and not 300 or not 500)  #False
