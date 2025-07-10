# concession stand program

menu = {
    "pizza" : 50.00,
    "nachos" :  35.50,
    "popcorn" : 20.00,
    "fries" : 18.99,
    "chips": 12.99,
    "pretzel" : 20.00,
    "soda": 18.00,
    "coke": 18.99
}

cart = []
total = 0

print('----------Menu-----------')
for key, value in menu.items():
    print(f"{key:10} : R{value:.2f}")
print('-------------------------')


while True:
    food = input("Select an item(q to quit): ").lower()
    if food == 'q':
        break
    elif menu.get(food) is not None:
        cart.append(food)
print('----------Your Order-----------')
for food in cart:
    total += menu.get(food)
    print(food, end=', ')

print()
print(f'TOTAL: R{total:.2f}')