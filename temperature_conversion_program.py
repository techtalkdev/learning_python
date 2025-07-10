#temperature conversion program

scale = input('Enter the scale[Degree/Fahrenheit] - (D/F) ').upper()

if scale == 'D':
    temperature = float(input('Enter your temperature in degrees: '))
    result = (temperature * 9 / 5) + 32
    print(f"The temperature is {round(result)} degrees Fahrenheit")
elif scale == 'F':
    temperature = float(input('Enter your temperature in Fahrenheit: '))
    result = (temperature - 32) * 5 / 9
    print(f"The temperature is {round(result)} degrees celsius")
else:
    print('Invalid scale')