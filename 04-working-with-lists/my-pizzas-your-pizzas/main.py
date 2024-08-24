pizzas = ["margherita","pepperoni","marinara"]

# copy pizzas list using slice
friend_pizzas = pizzas[:]

# add new pizza to pizzas list
pizzas.append("hawaiian")

# add new pizza to friend pizzas list
friend_pizzas.append("BBQ chicken")

# print pizzas list
print("My favorite pizzas are: ")
for pizza in pizzas:
    print(f"{pizza.title()}")

# print friend pizzas list
print()
print("My friend’s favorite pizzas are: ")
for friend_pizza in friend_pizzas:
    print(f"{friend_pizza.title()}")