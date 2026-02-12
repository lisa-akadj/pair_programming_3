class Playlist():
   
   def __init__(self):
      self.tracks = []

   def add(self, song):
      self.song = song 
      self.tracks.append(song)


   def list_of_tracks(self):
      if self.tracks == []:
         raise TypeError("list is empty")
      return list(self.tracks)