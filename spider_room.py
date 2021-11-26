#import the function defined in game_over.py
from game_over import game_over

# import the function defined in trophy_room.py
from trophy_room import trophy_room

# spider room
def spider_room():
    # give the prompts
    prompt =  """
            There is a spider here.
            Behind the spider is another door. 
            The spider is eating goat
            What would you do (1 or 2)
            (1) Fight the spider.
            (2) Taunt the spider. """
    
    print(prompt)

    # take the input()
    answer = input(">")

    if answer == "1":
        # the player is dead
        game_over("The spider killed you.")

    elif answer == "2":
        # send the player to the trophy room
        print("\nThe spider was so impressed with your taunting skills he lets you pass through the door.")
        trophy_room()