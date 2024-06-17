
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import env as env
# Replace these with your own credentials
client_id = env.client_id
client_secret = env.client_secret
redirect_uri = env.redirect_url

# Define the scope
scope = 'user-library-read'

# Authenticate with Spotify using Client Credentials Flow
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id,
                                                           client_secret=client_secret))

# Function to get Spotify URL for a song
def get_spotify_url(song_name, album_name):
    query = f"track:{song_name} album:{album_name}"
    results = sp.search(q=query, type='track', limit=1)
    if results['tracks']['items']:
        track = results['tracks']['items'][0]
        return track['external_urls']['spotify']
    else:
        return None

# Example usage
song_name = "thoogu manchadalli koothu"
album_name = "kirik party"
url = get_spotify_url(song_name, album_name)
if url:
    print(f"The Spotify URL for '{song_name}' from the album '{album_name}' is: {url}")
else:
    print("Song not found.")

# https://open.spotify.com/track/4dIP90GhOQHScQ53XPFml2?si=8112339faf15414d
# The Spotify URL for 'anisuthide' from the album 'mungaru male' is: https://open.spotify.com/track/4dIP90GhOQHScQ53XPFml2