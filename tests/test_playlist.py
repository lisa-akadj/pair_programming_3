from lib.playlist import *

def test_add_song():
    playlist = Playlist()
    playlist.add("Umbrella by Rihanna")
    assert playlist.tracks == ['Umbrella by Rihanna']