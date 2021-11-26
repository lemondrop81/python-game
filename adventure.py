#import the function defined in spider_room.py
from spider_room import *

def start():
    # give the inital prompts.
    print("\nYou are standing in a dark and creepy hallway.")
    print("There is a door to your left, another to the right and a hallway straight ahead. Which way do you go? (l, r or s)")

    # convert the player's input() to lower_case
    answer = input(">").lower()

    if "l" in answer:
        # if the player typed "left" or "l" lead him to the spider_room()
        spider_room()



# starting the game
start()