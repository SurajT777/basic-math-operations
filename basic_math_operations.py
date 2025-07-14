# basic python operation
# getting input from the user

num1 = float(input("enter the first number:"))
num2 = float(input("enter the second number:"))

print("****************************************")

addition = num1 + num2
subtraction = num1 - num2
divide = num1 / num2 if num2 != 0 else "Error : Number can't be divided by zero" 
multiply = num1 * num2

print(f'\nAddition: {addition}')
print(f'\nsubtraction: {subtraction}')
print(f'\ndivide: {divide}')
print(f'\nmultiply: {multiply}')