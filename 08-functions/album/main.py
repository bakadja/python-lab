def  make_album(name,title,songs=None):
    """"The function should take in an artist name and an album title, and 
    it should return a dictionary containing these two pieces of information."""

    if songs:
        return {"name":name,"title":title, "songs":songs}

    return {"name":name,"title":title}

# call the function
albums = []
title= "G.O.A.T. Featuring James T. Smith the Greatest of All Time"
albums.append(make_album("Eminem","The Marshall Mathers LP"))
albums.append(make_album("LL Cool J",title))
albums.append(make_album("Lil Wayne","Tha Carter III"))
albums.append(make_album("Adele","25",11))

#print all albums
print()
for album in albums:
    if "songs" in album.keys():
        message = f"Artist: {album["name"].title()}\n"
        message += f"Album Title: {album["title"].title()}\n"
        message += f"Number of Songs: {album["songs"]} tracks.\n"
    else:
        message = f"Artist: {album["name"].title()}\n"
        message += f"Album Title: {album["title"].title()}\n"
    
    print(message)

    
