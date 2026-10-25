age = int(input("Enter your age: "))
try:
    if age < 18:
        raise ValueError("Age must be 18 or above")
except ValueError as v:
    print("Error:", v)
else:
    print("You are Eligible.")

