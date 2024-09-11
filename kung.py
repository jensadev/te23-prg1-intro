# En version av kung king, nånting, högsta kortet vinner
# Två spelare
# Spelare 1 rullar tärning
# Spelare 2 rullar tärning
# Vem rullade högst
# Högst vinner rundan
# Upprepa, till vi har en vinnare av spelet, bäst av tre

from random import randint

play_game = "J"

while play_game.upper() == "J":
    player_one_roll = randint(1, 6)
    player_two_roll = randint(1, 6)

    if player_one_roll > player_two_roll:
        print(f"Spelare ETT vinner med tärningskastet: {player_one_roll} över {player_two_roll}.")
    elif player_two_roll > player_one_roll:
        print(f"Spelare TVÅ vinner med tärningskastet: {player_two_roll}.")
    else:
        print(f"Ingen spelare vinner, det är oavgjort med tärningskastet: {player_one_roll}.")

    play_game = input("Vill du spela igen? [J/N]: ")

# att göra, komma ihåg vilken spelare som har vunnit
# spela tills vi har en bäst av tre
# sedan fråga om vi vill spela igen
