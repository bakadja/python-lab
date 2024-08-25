leonardo = {
    "first_name": "leonardo",
    "last_name": "da vinci",
    "age": 67,
    "city": "vinci", 
    "country": "italy",   
}

issac = {
    "first_name": "isaac",
    "last_name": "newton",
    "age": 84,
    "city": "woolsthorpe",
    "country": "england"
}

marie = {
    "first_name": "marie",
    "last_name": "curie",
    "age": 66,
    "city": "paris",
    "country": "france"
}

# print(issac)
people = [leonardo,issac,marie]

for person in people:
    print()
    for key, value in person.items():
        is_number = type(value) == int
        if is_number:
            print(f"{key}: {value}")
        else:
            print(f"{key}: {value.title()}")
    print()