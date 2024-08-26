def  make_shirt(size,text):
    """The function print a sentence summarizing the size of the shirt 
    and the message printed on it."""
    
    message = f"The shirt is available in {size} size"
    message += f" and it features the message: “{text}.”"
    print(message)

make_shirt("medium","Adventure Awaits")
print()
make_shirt(size="medium",text="Adventure Awaits")