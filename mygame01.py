#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""

def showInstructions():
    """Show the game instructions when called"""
    # print a main menu and the commands
    print('''
    RPG Game
    ========
    Get to the Garden with a key and a potion to win! Avoid the monsters! Commands include go [direction] and get [item].
    ''')

def showStatus():
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # ADDED ROOM DESCRIPTION 
    print('Room Description:')
    for direction, room in rooms[currentRoom].items():
        if direction != 'item':
            print(f"To the {direction.capitalize()} is the {room}")
    
    print('Inventory:', inventory)

    # Check if 'item' key exists and is not None
    if 'item' in rooms[currentRoom] and rooms[currentRoom]['item'] is not None:
        print('You see a ' + rooms[currentRoom]['item'])
    else:
        print('There is nothing of interest here.')

    print("---------------------------")


# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
rooms = {
    'Hall': {
        'south': 'Kitchen',
        'east': 'Dining Room',
        'west': 'Bedroom',
        'item': 'key'
    },

    'Kitchen': {
        'north': 'Hall',
        'item': 'monster',
    },
    'Dining Room': {
        'west': 'Hall',
        'south': 'Garden',
        'item': 'potion'
    },
    'Garden': {
        'north': 'Dining Room',
        'item': None  # No item in the garden
    },
    'Bedroom': {  # ADDED NEW ROOM
        'east': 'Hall',
        'item': None  # No item in the bedroom
    }
}

# start the player in the Hall
currentRoom = 'Hall'
moves = 0  # ADDED MOVES COUNTER

showInstructions()

# breaking this while loop means the game is over
while True:
    showStatus()
    moves += 1  # Increment moves counter

    move = input('>').lower().split(" ", 1)

    if move[0] == 'go':
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
        else:
            print('You can\'t go that way!')

    if move[0] == 'get':
        if currentRoom in rooms and 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            inventory.append(move[1])
            print(move[1] + ' got!')
            del rooms[currentRoom]['item']
        else:
            print('Can\'t get ' + move[1] + '!')

    if currentRoom in rooms and rooms[currentRoom].get('item') is not None:
        if 'monster' in rooms[currentRoom]['item']:
            print('A monster has got you... GAME OVER!')
            break

    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break

print("Total moves made:", moves)




