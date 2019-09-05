# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:

    def __init__(self, name, currRoom):
        self.name = name
        self.currRoom = currRoom
        # self.inv = inv

    def __str__(self):
        return f"Player: {self.name}\nCurrent Room: {self.currRoom}"

    def __repr__(self):
        return f'Player: {repr(self.name)}\n{repr(self.currRoom)}'

    def change_rooms(self, room):
        self.room = room
