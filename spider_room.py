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