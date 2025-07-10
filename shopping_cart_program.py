#⭐ shopping cart program 🛒

foods = []
prices = []
total = 0

while True:
    food = input('Enter the food you want to buy(press q to quit): ')
    if food == '': break
    if food.lower() == 'q':
        break
    else:
        price = float(input(f'Enter the price of {food}:R '))
        if price == '': break
        foods.append(food)
        prices.append(price)



print('----------YOUR CART----------')

for food in foods:
    print(food, end= ', ')

for price in prices:
  total += price

print()
print(f"Your total is: R{total}")