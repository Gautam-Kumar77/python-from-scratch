#There are four ways/methods/logic to swap the number

#Method 1
a=10
b=20
a,b=b,a
print("Value of a= {} \nValue of b= {} " .format(a,b))

#Method 2
a=10
b=20

print("="*40)
print("Value of a= {} \nValue of b= {} " .format(a,b))
temp=a
a=b
b=temp
print("Values after Swapping")
print("Value of a= {} \nValue of b= {} " .format(a,b))

#Method 3
a=2
b=3

a= a+b
b= a-b
a= a-b
print("="*40)
print("Value of a= {} \nValue of b= {} " .format(a,b))

#Method 4
a=5
b=6
a=a*b
b= a//b
a= a//b
print("="*40)
print("Value of a= {} \nValue of b= {} " .format(a,b))
print("="*40)
#Method 5
a=2
b=3
a= a^b
b= a^b
a= a^b
print(a,b)