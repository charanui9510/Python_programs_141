a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))

print(f"a value is : {a}")
print(f"b value is : {b}")
print(a,b)
a,b = b,a
print(f"Value of a is : {a}\nValue of b is : {b}")
