def  make_album(name,title,songs=None):
    """"The function should take in an artist name and an album title, and 
    it should return a dictionary containing these two pieces of information."""

    if songs:
        return {"name":name,"title":title, "songs":songs}

    return {"name":name,"title":title}

# ask user input
album_artist_prompt="\nalbum’s artist: "
title_prompt="album’s title: "
quit_prompt="\ndo you want to continue yes/no?: "
albums_list= []

while True:
    name = input(album_artist_prompt)
    title = input(title_prompt)
    print()

    album = make_album(name,title)
    albums_list.append(album)
        
    # retrieve all album in album dictionary
    for item in albums_list:
        for key, value in item.items():
            message = f"{key.title()}: {value.title()}"
            print(message)
        print()
    
    quit = input(quit_prompt)
    if quit.lower() in ["yes","ya","y"]:
        continue
    else:
        break


    
