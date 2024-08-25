prompt = "If you could visit one place in the world, "
prompt += "where would you go? "
users = {}
count = 0

while True:
    request = input(prompt)
    person = f"person-{count}"
    users[person] = request

    new_request = input("do you want to continue?: yes / no ")
    if new_request in ['yes',"ja","y"]:
        count += 1
        continue
    else:
        print("\nThank you for your participation")
        break

print("Result:")
for person, city in users.items():
    print(f"{person}: {city.title()}") 