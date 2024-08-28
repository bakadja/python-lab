class User:
    """represent a user."""
    def __init__(self,first_name,last_name):
        """initialize attributes to describe a user."""
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        """print a summary of the user's information."""
        summary = f"Firstname: {self.first_name.title()}\n"
        summary += f"Lastname: {self.last_name.title()}\n"
        print(summary)

    def greet_user(self):
        """print a personalized greeting to the user."""
        message = f"Hi {self.first_name.title()} {self.last_name.title()}, "
        message += f"we're thrilled to have you here. Enjoy your time with us, "
        message += f"and let us know if you need anything!\n"
        print(message)

# instances for class
user_1 = User("john","doe")
user_2 = User("jane","doe")

#call the methods
user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()