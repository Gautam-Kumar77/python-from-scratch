''' Q.1 Addition

Create two variables:
num1 = 15
num2 = 25
Store their sum in another variable and print it. '''

num1= 15
num2=25
sum= num1+num2
print(sum)

''' Q2. Rectangle Area
Store:
Length = 15
Width = 8
Calculate: Area
Print the result. '''

Length= 15
Width = 8
Area= Length*Width
print(Area)

''' Q3. Temperature
Store temperature in Celsius.
Convert it to Fahrenheit.'''

Celsius = 25
Fahrenheit = (Celsius * 9/5) + 32
print(Fahrenheit)

# Q4, Swap values without third variable

a= 10
b= 5
a , b = b, a
print(a,b)

num1= int(input("Enter a number:"))
num2= int(input("Enter 2nd number:"))
num1, num2= num2, num1
print(f'Num1 is:- {num1} and Num2 is:- {num2}')
