# var_name=bool(int/float/complex/str)

                             #RULES
# This Function is  Used for Converting the Possible Type of Values into  bool type value
# ALL NON-ZERO VALUES ARE CONSIDERED AS TRUE
# ALL ZERO VALUES ARE CONSIDERED AS FALSE
# ALL NON-ZERO STRING LENGTH VALUES ARE CONSIDERED AS TRUE
# ALL ZERO  STRING LENGTH VALUES ARE CONSIDERED AS FALSE

#Example 1: int type value into bool type
# a= 123
# b= bool(a)
# print(b, type(b))      #True

# a= 0
# b= bool(a)
# print(b, type(b))     #False

#Example 2: float type value into bool type
# a= 123.23
# b= bool(a)
# print(b, type(b))

# a=0.0
# b= bool(a)
# print(b, type(b))

#Example 3: complex type value into bool type
# a= 23+2j
# b= bool(a)
# print(b)

#Example 4: str type value into bool type
# a= "PYTHON"
# b= bool(a)
# print(b, type(b))

# Case 1: str int value into bool type
# a= "3325"
# b= bool(a)
# print(b, type(b))

# Case 2: str float value into bool type
# a= "23.4"
# b= bool(a)
# print(b, type(b))

# Case 3: str complex value into bool type
# a= 2+1j
# b= bool(a)
# print(b, type(b))

#  Case 4: pure str  value into bool type
# a="PYTHON"
# b= bool(a)
# print(b, type(b))