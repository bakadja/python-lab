guests = ["stanislas","robert","oussama"]

# add a new guest to the biginning of the List
guests.insert(0,"claudel")

# add a new guest to the middle of the List
guests.insert(2,"phillip")

# add a new guest to the end of the List
guests.append("aliko")


# informing people that i found a bigger table
print("Hi everyone, I’m sorry, but I just found out I can only invite two people for dinner. Thanks for understanding!")
print()

# append removed guest
removed_guests = [guests.pop(0),guests.pop(1),guests.pop(1),guests.pop(1)]
remove_guest_message = "I’m really sorry, but due to some unexpected changes, I’m not able to invite you to dinner this time. I hope we can get together soon. Thank you for understanding"

print(f"Hi {removed_guests[0].title()} {remove_guest_message}\n")
print(f"Hi {removed_guests[1].title()} {remove_guest_message}\n")
print(f"Hi {removed_guests[2].title()} {remove_guest_message}\n")
print(f"Hi {removed_guests[3].title()} {remove_guest_message}\n")

message = f"Dear {guests[0].title()} and {guests[1].title()} I’m so happy to have you here tonight. Thank you for coming to share this dinner with me. Please make yourselves at home, and let’s enjoy this evening together!"

print()
print(message)

#use del to remove last 2 guests
del guests[0]
del guests[0]

print()
print(guests)