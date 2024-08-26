def  make_car(manufacturer,model,**kwargs):
    """Build a dictionary containing everything we know about a car"""
    # |  merge operator (Python 3.9+  to combine two dictionaries
    return {
        "manufacturer" : manufacturer,
        "model": model,
    } | kwargs

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)