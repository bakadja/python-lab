cities = {
    "new york": {
        "country": "United States",
        "population": 8_400_000,
        "fact": "The Statue of Liberty is located in New York Harbor."
    },
    "tokyo": {
        "country": "Japan",
        "population": 9_700_000,
        "fact": "Tokyo is the most populous city in the world."
    },
    "paris": {
        "country": "France",
        "population": 2_150_000,
        "fact": "The Eiffel Tower was originally intended as a temporary structure."
    }
}

# all information for each city

for city in cities:
    print(f"\nInformation about {city.title()}:")
    city_info = cities[city]
    for key, value in city_info.items():
        print(f"{key}: {value}")
    print()