import pytest
from lib.playlist import *

def test_add_song():
    playlist = Playlist()
    playlist.add("Umbrella by Rihanna")
    assert playlist.tracks == ['Umbrella by Rihanna']

def test_typerror_in_list_empty():
    playlist = Playlist()
    with pytest.raises(TypeError):
        playlist.list_of_tracks()
        
def test_when_list_is_not_empty():
    playlist = Playlist()
    playlist.add("Umbrella by Rihanna")
    result = playlist.tracks
    assert result == ["Umbrella by Rihanna"]