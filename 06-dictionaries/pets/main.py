pet1 = {
    "kind": "dog",
    "owner": "alice"
}

pet2 = {
    "kind": "cat",
    "owner": "bob"
}

pet3 = {
    "kind": "parrot",
    "owner": "charlie"
}

pet4 = {
    "kind": "rabbit",
    "owner": "diana"
}

pet5 = {
    "kind": "hamster",
    "owner": "eve"
}

# List of pets
pets = [pet1, pet2, pet3, pet4, pet5]

for pet in pets:
    for key, value in pet.items():
        print(f"{key.title()}: {value.title()}")
    print()
