current_users = ["PixelPioneer","NovaNerd","EchoExplorer","MysticMaverick",
"QuantumQuokka"]
new_users = ["talon45","NovaNerd","EchoExplorer","champagne34","QuantumQuokka"]

#  comparison is case insensitive turn copy list name to lower case
copy_current_users = [value.lower() for value in current_users]

message = " already exists, you need to enter a new username"
for new_user in new_users:
    if new_user.lower() in copy_current_users:
        print(f"{new_user.title()} {message}\n")
    else:
        print(f"{new_user.title()} is available\n")

