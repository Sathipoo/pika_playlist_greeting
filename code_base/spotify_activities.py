


import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import env as env
# Replace these with your own credentials
client_id = env.client_id
client_secret = env.client_secret
redirect_uri = "https://www.spotifycodes.com"





class spotifyze:
    def __init__(self) -> None:
        # Authenticate with Spotify using Client Credentials Flow
        self.sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id,
                                                           client_secret=client_secret))

    def get_spotify_url(self,song_name, album_name):
        query = f"track:{song_name} album:{album_name}"
        results = self.sp.search(q=query, type='track', limit=1)
        if results['tracks']['items']:
            track = results['tracks']['items'][0]
            return track['external_urls']['spotify']
        else:
            return None
        
    def create_playlist(self, playlist_name, track_urls, description):
        scope = 'playlist-modify-public'
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                            client_secret=client_secret,
                                                            redirect_uri=redirect_uri,
                                                            scope=scope))
        user_id = sp.current_user()['id']
        playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=True, description=description)
        track_ids = [self.get_track_id(url) for url in track_urls]
        self.sp.playlist_add_items(playlist_id=playlist['id'], items=track_ids)
        return playlist['external_urls']['spotify']

    def get_track_id(self, url):
        track_id = url.split('/')[-1].split('?')[0]
        return f'spotify:track:{track_id}'
    

