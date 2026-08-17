# var_name=int(float/bool/complex/str)

#Example 1:  Float type value into int type
# a= 12.34
# b= int(a)
# print(b)

#Example 2: bool type value into int type
# a= True
# b= int(a)
# print(b)

#Example 3: complex type value into int type
# a= 2+4j
# b= int(a)
# print(b) #TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'

# case 1: str int value into int type
# a= "16"
# b= int(a)
# print(b)
# case 2: str float value into int type
# a="12.3"
# b= int(a)
# print(b) #ValueError: invalid literal for int() with base 10: '12.3'

#case 3: str complex value into int type
# a= "23+3j"
# b= int(a)
# print(b) #ValueError: invalid literal for int() with base 10: '23+3j'

#case 4: str bool value into int type
# a= "True"
# b= int(a)
# print(b) #ValueError: invalid literal for int() with base 10: 'True'

#case 5: pure str value into int type
# a="PYTHON"
# b= int(a)
# print(b)  #ValueError: invalid literal for int() with base 10: 'PYTHON'

