countries = ["United States","China","Japan","Germany","India","United Kingdom","France","Canada","Italy","Brazil"] 

print(" The top three richest countries by GDP per capita (in USD) are\n")
for country in countries[:3]:
    print(country)

print("\nThe top three middle richest countries by GDP per capita (in USD) are\n")
for country in countries[3:6]:
    print(country)

print("\nThe three last middle richest countries by GDP per capita (in USD) are\n")
for country in countries[-3:]:
    print(country)