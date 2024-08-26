def describe_city(city, country="germany"):
    """The function print a simple sentence"""
    message = f"{city.title()} is in {country.title()}"
    print(message)

describe_city("berlin")
describe_city("münchen")
describe_city("paris","france")
