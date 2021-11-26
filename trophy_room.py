#import the function defined in game_over.py
from game_over import *

# trophy room
def trophy_room():
    # give the prompts
    prompt =  """
            You are now in a room filled with valuable trophies!
            There is a gold jewel encrusted door as well!
            What would you do? (1 or 2)
            (1). Take some trophies and go through the door.
            (2). Just go through the door. """
    
    print(prompt)

    #take imput()
    answer = input(">")

    if answer == "1":
        # the player dies from greed, and calls the game_over function.
        game_over("The trophies were cursed! The moment you touched one you were liquefied.")

    elif answer == "2":
        # the player won the game.
        print("\nNice, you are a honest person. Congrats you survived the horror.")

    else:
        # call game_over() with "reason"
        game_over("Go and learn how to type!")