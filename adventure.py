def start():
    # give the inital prompts.
    print("\nYou are standing in a dark and creepy hallway.")
    print("There is a door to your left, another to the right and a hallway in front of you. Which way do you go? (l, r or c)")

    # convert the player's input() to lower_case
    answer = input(">").lower()

    print(answer)



# starting the game
start()