places = {
    "john": ["paris","rome","turks & caicos"],
    "jane": ["glacier national park","maui","london"],
    "thomas": ["bora bora","swiss alps","maldives"],
}

for key, value in places.items():
    print(f"\n{key.title()} favorites's locations are: ")
    for place in value:
        print(place.title())
    print()
