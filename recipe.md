# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.


## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class Playlist():
    tracks_dict = {}
    # User-facing properties:
    #   name: string

    def __init__(self):
        # Parameters:
        #   name: string
        # Side effects:
        #   Sets the name property of the self object
        pass # No code here yet

    def add(self, title, artist):
        # Parameters:
        #   task: two string representing a title and artist
        # Returns:
        #   return a string which says: "You added {title} created by {artist} into your playlist."
        # Side-effects
        #   moving title and artist into our dictionary
        #.  throws an typeerror if music is duplicated
        pass # No code here yet

    def list_of_tracks(self):
        # Returns:
        #   Return the updated dictionary with the titles and artists
        # extra: if we want we can put a time and date on the returns
        # Side-effects:
        #   Throws an exception if no task is set
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given a song title and artist
Title and artist added to our list

"""
playlist = Playlist()
reminder.remind_me_to("Walk the dog")
reminder.remind() # => "Walk the dog, Kay!"

"""
Given a song title and artist
#"You added {title} created by {artist} into your playlist."
Throw a Typeerror if song is duplicated
"""
test_add = Playlist.add("Umbrella" "Rhianna")
reminder.remind()

"""
Given a song title and artist
#remind still reminds the user to do the task, even though it looks odd
"""
reminder = Reminder("Kay")
reminder.remind_me_to("")
reminder.remind() # => ", Kay!"
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
