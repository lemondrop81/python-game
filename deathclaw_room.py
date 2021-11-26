#import the function defined in game_over.py
from game_over import game_over

# import the function defined in trophy_room.py
from trophy_room import trophy_room

# deathclaw room
def deathclaw_room():
    # give the prompts
    prompt =  """
            You enter the room and see a sleeping deathclaw
            Behind the deathclaw is another door. 
            What would you do (1 or 2)
            (1) Go through the door silently.
            (2) Kill the deathclaw and show your bravery. """
    
    print(prompt)

    # take the input()
    answer = input(">")
    