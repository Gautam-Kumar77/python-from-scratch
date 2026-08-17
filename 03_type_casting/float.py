# var_name=float(int/bool/complex/str)

#Example 1:  int type value into float type
# a= 23
# b=float(a)
# print(b, type(b))

#Example 2:  bool type value into float type
# a= True
# b= float(a)
# print(b, type(b))

#Example 3:  complex type value into float type
# a= 3+2j
# b= float(a)
# print(b, type(b))  #TypeError: float() argument must be a string or a real number, not 'complex'

#case 1: str int value into float type
# a= "12"
# b= float(a)
# print(b, type(b))

#case 2: str float value into float type
# a= "123.67"
# b= float(a)
# print(b)

# #case 3: str bool value into float type
# a= "False"
# b = float(a)
# print(b)  #ValueError: could not convert string to float: 'False'

#case 4: str complex value into float type
# a= "2+2j"
# b= float(a)
# print(b)  #ValueError: could not convert string to float: '2+2j'

#case 5: str pure value into float value
# a= "PYTHON"
# b= float(a)
# print(b)  #ValueError: could not convert string to float: 'PYTHON'

