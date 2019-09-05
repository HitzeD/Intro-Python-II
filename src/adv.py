from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player1 = Player("John", room['outside'])

# print(player1)
# print(player1.currRoom.name)
quit = False

while not quit:

    print(f"\nName: {player1.name}")
    print(f"\nRoom: {player1.currRoom.name}\n")
    print(f"{player1.currRoom.description}\n")

    command = input("(N)orth\n(S)outh\n(E)ast\n(W)est\n(Q)uit\n\nCommand: ")
    command.lower().strip()[0]

    if command == 'q':
        quit = True

    if command == 's':

        new_loc = player1.currRoom.switch_direction(command)

        if new_loc == None:
            print('Thou shall not pass (this way at least!)')
        else:
            player1.change_rooms(new_loc)

    if command == 'n':

        new_loc = player1.currRoom.switch_direction(command)
        
        if new_loc == None:
            print('Thou shall not pass (this way at least!)')
        else:
            player1.change_rooms(new_loc)

    if command == 'w':

        new_loc = player1.currRoom.switch_direction(command)

        if new_loc == None:
            print('Thou shall not pass (this way at least!)')
        else:
            player1.change_rooms(new_loc)

    if command == 'e':
        new_loc = player1.currRoom.switch_direction(command)

        if new_loc == None:
            print('\nThou shall not pass (this way at least!)\n')
        else:
            player1.change_rooms(new_loc)


# Write a loop that:
#  
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
