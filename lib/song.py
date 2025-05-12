import ipdb

class Song:
    
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    
    def __init__(self, name, artist, genre):
        self.name= name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count(self)
        Song.add_to_genres(self)
        Song.add_to_artists(self)
        Song.add_to_genre_count(self)
        Song.add_to_artist_count(self)
        
    @classmethod
    def add_to_genre_count(cls, song):
        # ipdb.set_trace()
        num = 1 if song.genre not in cls.genre_count.keys() else cls.genre_count[song.genre] + 1
        cls.genre_count.update({song.genre: num})  
        
    @classmethod
    def add_to_artist_count(cls, song):
        num = 1 if song.artist not in cls.artist_count.keys() else cls.artist_count[song.artist] + 1
        cls.artist_count.update({song.artist: num})   
  
    @classmethod      
    def add_song_to_count(cls, song):
        cls.count += 1
        
    @classmethod
    def add_to_genres(cls, song):
        cls.genres.append(song.genre) if song.genre not in cls.genres else None
        
    @classmethod
    def add_to_artists(cls, song):
        cls.artists.append(song.artist) if song.artist not in cls.artists else None