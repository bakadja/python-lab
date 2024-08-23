guests = ["stanislas","robert","oussama"]

new_guest = "stephanie" 
absent_guest = guests.pop(1)

# add new guest in guests list
guests.append(new_guest)
message = f"Dear {guests[0].title()},{guests[1].title()} and {guests[2].title()} I’m so happy to have you here tonight. Thank you for coming to share this dinner with me. Please make yourselves at home, and let’s enjoy this evening together!"
print(message)

# print absent guest
print()
print(absent_guest.title())