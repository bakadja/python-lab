sandwich_orders = [
    "blt",
    "turkey club",
    "grilled cheese",
    "reuben",
    "philly cheesesteak",
    "veggie wrap",
    "tuna salad",
    "pastrami",
    "pastrami",
    "pastrami"
]

print("\nthe deli has  run out of pastrami")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove("pastrami")

print("\nnew menu:")
for sandwich in sandwich_orders:
    print(f"\t{sandwich}")
