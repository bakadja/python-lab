def show_messages(messages):
    """ prints text message"""
    for message in messages:
        print(message)

def  send_messages(messages):
    """ prints each text message and moves each message to a new list"""
    sent_messages = []
    while messages:
        removed_message = messages.pop(0)
        print(removed_message)
        sent_messages.append(removed_message)
    
        

positive_messages = [
    "You're such an inspiration!",
    "You're doing great!",
    "Let me know if I can help in any way.",
    "Your presence is a present to the world.",
    "You've got this.",
    "You are strong and can do this.",
    "I'm here for you."
]

send_messages(positive_messages[:])
print()
show_messages(positive_messages)