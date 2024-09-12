# En version av kung king, nånting, högsta kortet vinner

# Två spelare

# Spelare 1 rullar tärning

# Spelare 2 rullar tärning

# Vem rullade högst

# Högst vinner rundan

# Upprepa, till vi har en vinnare av spelet, bäst av tre


from random import randint

RUN = "J"

PLAYER_ONE_SCORE = 0  # initiera innan loopen för att den ska kunna behålla värdet

PLAYER_TWO_SCORE = 0  # snake_case

GAME_ROUND = 0


while RUN.upper() == "J":

    GAME_ROUND += 1

    player_one_roll = randint(1, 6)

    player_two_roll = randint(1, 6)


    if player_one_roll > player_two_roll:

        print(

            f"Spelare ETT vinner med tärningskastet: {player_one_roll}"

            " över {player_two_roll}."

        )

        PLAYER_ONE_SCORE += 1

    elif player_two_roll > player_one_roll:

        print(f"Spelare TVÅ vinner med tärningskastet: {player_two_roll}.")

        PLAYER_TWO_SCORE += 1

    else:

        print(

            f"Ingen spelare vinner, det är oavgjort med tärningskastet: {player_one_roll}."

        )


    if PLAYER_ONE_SCORE >= 2:

        print(

            f"Efter {GAME_ROUND} rundor vann spelare ett med {PLAYER_ONE_SCORE} "

            "över {PLAYER_TWO_SCORE}."

        )
        RUN = "n"

    elif PLAYER_TWO_SCORE >= 2:

        print(

            f"Efter {GAME_ROUND} rundor vann spelare två med {PLAYER_TWO_SCORE} "

            "över {player_one_score}."

        )
        RUN = "n"

    elif GAME_ROUND >= 3:

        print(

            f"Efter {GAME_ROUND} rundor har ingen spelare vunnit. Poängen för "

            "spelare ett är: {player_one_score} och för spelare två: {player_two_score}."

        )
        RUN = "n"


    # play_game = input("Vill du spela igen? [J/N]: ")


# att göra, komma ihåg vilken spelare som har vunnit

# spela tills vi har en bäst av tre

# sedan fråga om vi vill spela igen
