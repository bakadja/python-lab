def ordered_sandwich(*args):
    """ should print a summary of the sandwich that’s being ordered."""
    message = f"\nsummary of the {len(args)} sandwiches being ordered:"
    print(message)
    print()
    for sandwich in args:
        print(f"{sandwich.title()}")

ordered_sandwich("BLT","Turkey Club","Grilled Cheese","Reuben")
ordered_sandwich("BLT","Turkey Club","Grilled Cheese")
ordered_sandwich("BLT","Turkey Club")