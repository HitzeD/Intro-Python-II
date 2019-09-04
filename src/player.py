# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:

    def __init__(self, name, currRoom, inv):
        self.name = name
        self.currRoom = currRoom
        self.inv = inv
