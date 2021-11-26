# import the function defined in game_over.py
from game_over import game_over

# vampire room
def vampire_room():
    # give the prompts
    prompt =  """
            You spot a vampire sitting in a library.
            The vampire invites you to sit down and join him in reading
            What would you do (1, 2 or 3)
            (1). Sit down and join the vampire.
            (2). Attack the vampire with a wooden stake.
            (3). Turn around and head back through the only door in the room """
    
    print(prompt)

    # take the input()
    answer = input(">")

    if answer == "1":
        # call game_over() with "reason"
        game_over("You spend eternity in an enchanted bliss reading.")

    elif answer == "2":
        # call game_over() with "reason"
        game_over("The Lich librarian kills you for making noise")

    elif answer == "3":
        # call game_over() with "reason"
        game_over("The vampire attacks you while your back is turned")
    
    else:
        # call game_over() with "reason"
        game_over("Go and learn how to type!")