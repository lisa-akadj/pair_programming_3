import pytest
from lib.playlist import *

def test_add_song():
    playlist = Playlist()
    playlist.add("Umbrella by Rihanna")
    assert playlist.tracks == ['Umbrella by Rihanna']

def test_typerror_in_list_empty():
    playlist = Playlist()
    with pytest.raises(TypeError):
        playlist.add()
    assert playlist.list_of_tracks == "Playlist is empty"
        