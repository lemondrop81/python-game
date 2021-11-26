# import the function defined in spider_room.py
from spider_room import spider_room

# import the function defined in deathclaw_room.py
from deathclaw_room import deathclaw_room

# import the function defined in vampire_room.py
from vampire_room import vampire_room

# import the function defined in game_over.py
from game_over import game_over

def start():
    # give the inital prompts.
    print("\nYou are standing in a dark and creepy hallway.")
    print("There is a door to your left, another to the right and a hallway straight ahead. Which way do you go? (l, r or s)")

    # convert the player's input() to lower_case
    answer = input(">").lower()

    if "l" in answer:
        # if the player typed "left" or "l" lead him to the spider_room()
        spider_room()
    
    elif "r" in answer:
        # else if the player typed "right" or "r" lead him to the deathclaw_room()
        deathclaw_room()

    elif "s" in answer:
        # else if the player typed "straight" or "s" lead him to the vampire_room()
        vampire_room()

    else:
        # else call game_over() function with the "reason" argument
        game_over("Don't you know how to type something properly>")


# starting the game
start()