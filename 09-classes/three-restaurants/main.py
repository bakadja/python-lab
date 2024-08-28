class Restaurant:
    """represent a restaurant with name and cuisine_type"""
    def __init__(self,restaurant_name, cuisine_type):
        """init the 2 attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """print the two attributes """
        message = f"Restaurant Name: {self.restaurant_name.title()}" 
        message += f"\tCuisine typ: {self.cuisine_type.title()}"
        print(message)
    
    def open_restaurant(self):
        """indicating that the restaurant is open"""
        message=f"\nwe're open!"
        print(message)

# make an instance from my class
restaurant = Restaurant("bistro belle","la dolce vita")
favorite_restaurant = Restaurant("flavor fusion","spice route")
my_restaurant = Restaurant("harvest feast","el pueblo")

#call both methods
print()
restaurant.describe_restaurant()
favorite_restaurant.describe_restaurant()
my_restaurant.describe_restaurant()



