# En version av kung king, nånting, högsta kortet vinner
# Två spelare
# Spelare 1 rullar tärning
# Spelare 2 rullar tärning
# Vem rullade högst
# Högst vinner rundan
# Upprepa, till vi har en vinnare av spelet, bäst av tre

from random import randint

play_game = "J"
player_one_score = 0  # initiera innan loopen för att den ska kunna behålla värdet
player_two_score = 0  # snake_case
game_round = 0

while play_game.upper() == "J":
    game_round += 1
    player_one_roll = randint(1, 6)
    player_two_roll = randint(1, 6)

    if player_one_roll > player_two_roll:
        print(
            f"Spelare ETT vinner med tärningskastet: {player_one_roll} över {player_two_roll}."
        )
        player_one_score += 1
    elif player_two_roll > player_one_roll:
        print(f"Spelare TVÅ vinner med tärningskastet: {player_two_roll}.")
        player_two_score += 1
    else:
        print(
            f"Ingen spelare vinner, det är oavgjort med tärningskastet: {player_one_roll}."
        )

    if player_one_score >= 2:
        print(f"Efter {game_round} rundor vann spelare ett med {player_one_score} över {player_two_score}.")
        play_game = "n"
    elif player_two_score >= 2:
        print(f"Efter {game_round} rundor vann spelare två med {player_two_score} över {player_one_score}.")
        play_game = "n"
    elif game_round >= 3:
      print(f"Efter {game_round} rundor har ingen spelare vunnit. Poängen för spelare ett är: {player_one_score} och för spelare två: {player_two_score}.")
      play_game = "n"

    # play_game = input("Vill du spela igen? [J/N]: ")

# att göra, komma ihåg vilken spelare som har vunnit
# spela tills vi har en bäst av tre
# sedan fråga om vi vill spela igen
