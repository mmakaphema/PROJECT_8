#   A SHOPPING CART PROGRAMME

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy or press q to quit:")
    if food.lower() == 'q':
     break
    else:
        price = float(input(f"Enter the price of the {food}: R"))
        foods.append(food)
        prices.append(price)
        print("-----YOUR CART🛒🤸-----")
    
    for food in foods:
        print(food, end= " ")
        
    total = 0
    for price in prices:
        total += price
    print("\n")
    print(f"Your total is: R{total}")