from lib.playlist import *

def test_example():
    assert True
def test_new_song_added():
    playlist = Playlist()
    result = playlist.add("Umbrella", "Rihanna")
    #updated_list = Playlist().tracks_dict = {"Umbrella" : "Rihanna"}
    #assert result == "You added Umbrella created by Rihanna into your playlist."
