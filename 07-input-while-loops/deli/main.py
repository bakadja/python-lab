sandwich_orders = [
    "BLT",
    "Turkey Club",
    "Grilled Cheese",
    "Reuben",
    "Philly Cheesesteak",
    "Veggie Wrap",
    "Tuna Salad",
    "Pastrami on Rye",
    "Cuban Sandwich"
]
finished_sandwiches = []

print("I made your:")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(current_sandwich.title())
    finished_sandwiches.append(current_sandwich)

print("\nlisting of sandwich that was made:")
for sandwich in finished_sandwiches:
    print(sandwich.title())
    
