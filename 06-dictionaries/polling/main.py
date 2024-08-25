favorite_languages = {    
    'jen': 'python',    
    'sarah': 'c',    
    'edward': 'rust',    
    'phil': 'python',    
}

peoples = ["tim","jen","john","sarah"]
for people in peoples:
    if people in favorite_languages.keys():
        message = "Thank you so much, I truly appreciate your participation."
        print(f"Dear {people},\n{message}\n")
    else:
        message = """We’d love to hear your thoughts! Please take a moment 
        to participate in our poll. Your input matters! 🙌"""
        
        print(f"Dear {people},\n{message}\n")
