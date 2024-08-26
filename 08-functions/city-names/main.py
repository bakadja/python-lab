def  city_country(city,country):
    """ The function return a string formatted city and country"""
    formatted_message = f"{city.title()}, {country.title()}"
    return formatted_message

# call the function
formatted_city_country = []
formatted_city_country.append(city_country("New York", "United States"))
formatted_city_country.append(city_country("Tokyo", "Japan"))
formatted_city_country.append(city_country("Paris", "France"))

#print the values
for value in formatted_city_country:
    print(f'"{value}"')


