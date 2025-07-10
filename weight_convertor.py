#Python Weight Convertor

mass_option = input('Enter Mass Option(KG/LBS): ').upper()

if mass_option == 'KG':
    weight =  float(input('Enter weight in kilograms: '))
    print(f'You are converting from kg to pounds')
    mass = weight * 2.205
    print(f"Its {round(mass)} Pounds")

elif mass_option == 'LBS':
     weight = float(input('Enter weight in Pounds: '))
     print(f'You are converting from kg to pounds')
     mass = weight / 2.205
     print(f"Its {round(mass)} Kg")
else:
    print('You entered something invalid')
