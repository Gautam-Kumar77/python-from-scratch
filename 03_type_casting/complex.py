# var_name=complex(int/float/bool/complex/str)

#Example 1: int type value into complex type
# a= 12
# b= complex(a)
# print(b, type(b))

#Example 2: float type value into complex type
# a= 12.3
# b= complex(a)
# print(b, type(b))

#Example 3: bool type value into complex type
# a= False
# b= complex(a)
# print(b, type(b))

# Case 1: str int type value into complex type
# a= "87"
# b= complex(a)
# print(b, type(b))

# Case 2: str float type value into complex type
# a= "87.45"
# b= complex(a)
# print(b, type(b))

# Case 3: str bool type value into complex type
# a= "True"
# b= complex(a)
# print(b, type(b))   #ValueError: complex() arg is a malformed string

# Case 4: str complex type value into complex type
# a= "13+4j"
# b= complex(a)
# print(b, type(b))

# Case 5: pure str type value into complex type
# a= "PYTHON"
# b= complex(a)
# print(b, type(b))  #ValueError: complex() arg is a malformed string
