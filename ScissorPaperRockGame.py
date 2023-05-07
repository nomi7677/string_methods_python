import random
def getChoices():
    player_choice= input("Enter your choice(rock, scissor or paper:) ")
    options=["rock", "paper", "scissor"]
    computer_choice=random.choice(options)
    choices = {"player": player_choice, "computer":computer_choice}
    return choices
choices= getChoices()
print(choices)