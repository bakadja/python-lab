def  make_shirt(size="Large",text="I love Python"):
    """The function print a sentence summarizing the size of the shirt 
    and the message printed on it."""
    
    print()
    message = f"The shirt is available in {size} size"
    message += f" and it features the message: “{text}.”"

    if size.lower() == "large" or size.lower() == "medium": 
        print(message)
        return
    
    message = f"The shirt comes in {size} size, and it proudly displays" 
    message += f"the message: “{text}.”"
    print(message)

make_shirt()
print()
make_shirt("medium")
print()
make_shirt(size="medium",text="Adventure Awaits")
print()
make_shirt(size="extra large",text="Explore the Unknown")
