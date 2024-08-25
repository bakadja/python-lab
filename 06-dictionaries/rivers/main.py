rivers = {
    "nile": "egypt",
    "amazon": "south america",
    "yangtze": "china",
}

for key,value in rivers.items():
    print(f"{key.title()} flowing through {value.title()}\n")

# name of each river 
for name in rivers.keys():
    print(name.title())

# country of each river, set to get unique value(avoid duplicate value)
print() 
for country in set(rivers.values()):
    print(country.title())