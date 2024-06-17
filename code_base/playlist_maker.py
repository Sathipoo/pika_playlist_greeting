import spotipy
from spotipy.oauth2 import SpotifyOAuth
from http.server import HTTPServer, BaseHTTPRequestHandler
import webbrowser
import env as env

# Replace these with your own credentials
client_id = env.client_id
client_secret = env.client_secret
redirect_uri = "http://localhost:8080"

# Define the scope
scope = 'playlist-modify-public'

class OAuthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Authentication successful. You can close this window.")
        # Extract the authorization code from the URL
        self.server.auth_code = self.path.split('code=')[1]

def start_local_server():
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, OAuthHandler)
    httpd.handle_request()  # Waits for a single request
    return httpd.auth_code

# Create SpotifyOAuth object
oauth = SpotifyOAuth(client_id=client_id,
                     client_secret=client_secret,
                     redirect_uri=redirect_uri,
                     scope=scope)

# Get the authorization URL and open it in a web browser
auth_url = oauth.get_authorize_url()
webbrowser.open(auth_url)

# Start the local server to handle the redirect and get the authorization code
auth_code = start_local_server()

# Use the authorization code to get an access token
token_info = oauth.get_access_token(auth_code)
access_token = token_info['access_token']

class spotifyze:
    def __init__(self, token):
        self.sp = spotipy.Spotify(auth=token)

    def get_spotify_url(self, song_name, album_name):
        query = f"track:{song_name} album:{album_name}"
        results = self.sp.search(q=query, type='track', limit=1)
        if results['tracks']['items']:
            track = results['tracks']['items'][0]
            return track['external_urls']['spotify']
        else:
            return None

    def create_playlist(self, playlist_name, track_urls, desc):
        user_id = self.sp.current_user()['id']
        playlist = self.sp.user_playlist_create(user=user_id, name=playlist_name, public=True, description=desc)
        track_ids = [self.get_track_id(url) for url in track_urls]
        self.sp.playlist_add_items(playlist_id=playlist['id'], items=track_ids)
        return playlist['external_urls']['spotify']

    def get_track_id(self, url):
        track_id = url.split('/')[-1].split('?')[0]
        return f'spotify:track:{track_id}'

# Example usage
spotify_instance = spotifyze(access_token)

# # Get Spotify URL for a specific song
# url = spotify_instance.get_spotify_url('Anisuthide', 'Mungaru Male')
# print("Spotify URL:", url)

# Create a playlist with a list of URLs
urls = [
    "https://open.spotify.com/track/4dIP90GhOQHScQ53XPFml2",
    "https://open.spotify.com/track/038gnuPve7s8rADCEDYsMH",
    "https://open.spotify.com/track/4y2TC8NVvWXfX3YL32qSEu",
    "https://open.spotify.com/track/2QIB7j35j3XFqrAPgZyBI3",
    "https://open.spotify.com/track/4k9RLcTWZog34sIXt23Ibr"
]
playlist_name = "To Pooja from Sathish"
description = "Craeted by Pikachooz"

playlist_url = spotify_instance.create_playlist(playlist_name, urls, description)
print("Playlist URL:", playlist_url)