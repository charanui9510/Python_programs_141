#ADDTION

num1 = float(input("Enter the first number : "))
num2 = float(input("Enter the second number : "))

# sum = num1 + num2
# print(int(sum))

sum_result = num1 + num2
multi_result = num1 * num2
print(f"sum: {num1} + {num2} = {sum_result}")
print(f"multiplication : {num1} * {num2} = {multi_result}") # Multiplication

#DIVISION

num3 = float(input("Enter the dividend for division : "))
num4 = float (input("Enter the divisor forf division: "))

if num4 == 0:
    print("Divisible by 'zero' is not possible")
else:
    div_result = num3/num4
    print(f"dividision : {num3} / {num4} = {div_result}")
