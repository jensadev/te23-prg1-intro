# En version av kung king, nånting, högsta kortet vinner
# Två spelare
# Spelare 1 rullar tärning
# Spelare 2 rullar tärning
# Vem rullade högst
# Högst vinner rundan
# Upprepa, till vi har en vinnare av spelet, bäst av tre

"""Using randint from random module"""
from random import randint

RUN = True
PLAYER_ONE_SCORE = 0  # initiera innan loopen för att den ska kunna behålla värdet
PLAYER_TWO_SCORE = 0  # snake_case
GAME_ROUND = 0


while RUN:
    GAME_ROUND += 1
    player_one_roll = randint(1, 6)
    player_two_roll = randint(1, 6)

    if player_one_roll > player_two_roll:
        print(f"Spelare ETT vinner med tärningskastet: {player_one_roll}"
        f" över {player_two_roll}.")

        PLAYER_ONE_SCORE += 1

    elif player_two_roll > player_one_roll:
        print(f"Spelare TVÅ vinner med tärningskastet: {player_two_roll}.")

        PLAYER_TWO_SCORE += 1

    else:
        print(f"Ingen spelare vinner, det är oavgjort med tärningskastet: {player_one_roll}.")

    if PLAYER_ONE_SCORE >= 2:
        print(f"Efter {GAME_ROUND} rundor vann spelare ett med {PLAYER_ONE_SCORE} "
        f"över {PLAYER_TWO_SCORE}.")

        RUN = False

    elif PLAYER_TWO_SCORE >= 2:
        print(f"Efter {GAME_ROUND} rundor vann spelare två med {PLAYER_TWO_SCORE} "
        f"över {PLAYER_ONE_SCORE}.")

        RUN = False

    elif GAME_ROUND >= 3:
        print(f"Efter {GAME_ROUND} rundor har ingen spelare vunnit. Poängen för "
        f"spelare ett är: {PLAYER_ONE_SCORE} och för spelare två: {PLAYER_TWO_SCORE}.")

        RUN = False

    if RUN is False:
        play_again = input("Vill du spela en omgång till? [Y/n]")
        if play_again.lower() == "y" or play_again == "":
            RUN = True
