import read_mongo
from  spotify_activities import spotifyze


reader = read_mongo.read_json()
song_group = reader.get_song_groups()


# print(song_group)

def get_song_url(song_name,album_name):
    sp = spotifyze()
    url = sp.get_spotify_url(song_name, album_name)
    if url:
        print(f"The Spotify URL for '{song_name}' from the album '{album_name}' is: {url}")
    else:
        print("URL not found for '{song_name}' from the album '{album_name}'.")
    return(url)

def create_playlist(playlist_name, urls, description):
    spotify_instance = spotifyze()
    playlist_url = spotify_instance.create_playlist(playlist_name, urls, description)
    print("Playlist URL:", playlist_url)
    return (playlist_url)

# for i in range(len(song_group)):
#     gr=song_group[i]
#     song=gr['song']
#     movie=gr['movie']
#     message=gr['message']
#     url = get_song_url(song,movie)
#     gr.update({"url":url})
    
# print(song_group)

urls = reader.get_urls()
print(urls)

playlist_name = "To Pooja from Sathish"
description = "Craeted by Pikachooz"

create_playlist(playlist_name, urls, description)