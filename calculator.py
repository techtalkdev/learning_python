#Python Calculator

operator = input('Enter an operator(+, -, * /): ')
first_number = float(input('Enter a first number: '))
second_number = float(input('Enter a second number: '))


if operator == '+':
    result = first_number + second_number
    print(result)
elif operator == '-':
    result = first_number - second_number
    print(result)
elif operator == '*':
    result = first_number * second_number
    print(result)
elif operator == '/':
    result = first_number / second_number
else:
    print('Invalid operator')