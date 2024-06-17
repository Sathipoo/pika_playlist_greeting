import json


class read_user_det:
    def __init__(self, user_det) -> None:
        self.data = user_det
    
    def get_data(self):
        return self.data
    
    def get_songs(self):
        songs = {}
        for key, value in self.data.items():
            if key.startswith('song'):
                song_number = key.replace('song', '')
                songs[song_number] = value
        return songs

    def get_messages(self):
        messages = {}
        for key, value in self.data.items():
            if key.startswith('mess'):
                message_number = key.replace('mess', '')
                messages[message_number] = value
        return messages

    def get_movies(self):
        movies = {}
        for key, value in self.data.items():
            if key.startswith('movie'):
                movie_number = key.replace('movie', '')
                movies[movie_number] = value
        return movies

    def get_song_groups(self):
        song_groups = []
        for i in range(1, 6):  # Assuming there are 5 song groups
            song_group = {
                'song': self.data.get(f'song{i}'),
                'movie': self.data.get(f'movie{i}'),
                'message': self.data.get(f'mess{i}')
            }
            song_groups.append(song_group)
        return song_groups
    
    def get_grouped_data(self):
        return self.data.get('grouped', [])

    def get_urls(self):
        urls = []
        grouped_data = self.get_grouped_data()
        for group in grouped_data:
            urls.append(group.get('url'))
        return urls

# # Example usage
# reader = read_json()

# # Get all data
# print("All data:", reader.get_data())

# # Get all songs
# print("Songs:", reader.get_songs())

# # Get all messages
# print("Messages:", reader.get_messages())

# # Get all movies
# print("Movies:", reader.get_movies())

# # Get all song groups
# print("Song Groups:", reader.get_song_groups())

# Get URLs from grouped data
# print("URLs:", reader.get_urls())
    
# ['https://open.spotify.com/track/4dIP90GhOQHScQ53XPFml2', 'https://open.spotify.com/track/038gnuPve7s8rADCEDYsMH', 'https://open.spotify.com/track/4y2TC8NVvWXfX3YL32qSEu', 'https://open.spotify.com/track/2QIB7j35j3XFqrAPgZyBI3', 'https://open.spotify.com/track/4k9RLcTWZog34sIXt23Ibr']