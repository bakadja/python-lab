guests = ["stanislas","robert","oussama"]

# add a new guest to the biginning of the List
guests.insert(0,"claudel")

# add a new guest to the middle of the List
guests.insert(2,"phillip")

# add a new guest to the end of the List
guests.append("aliko")

message = f"Dear {guests[0].title()},{guests[1].title()}, {guests[2].title()},{guests[3].title()},{guests[4].title()} and {guests[5].title()} I’m so happy to have you here tonight. Thank you for coming to share this dinner with me. Please make yourselves at home, and let’s enjoy this evening together!"

# informing people that i found a bigger table
print("Hi everyone, Good news! I managed to find a bigger table for our gathering. We’ll have plenty of space now to enjoy the evening comfortably. Looking forward to seeing you all soon!")
print()
print(message)


