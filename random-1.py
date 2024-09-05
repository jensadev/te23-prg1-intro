# # bestäm om det är udda eller jämnt
# # rulla tärningar
# # vinnaren är det som bestämts
# OM udda
# undersök om datorns tärning är udda
# undersök om spelarens tärning är udda

from random import randint

rule = input("Skriv om ni spelar udda eller jämnt: ")
computer = randint(1, 6)
player = randint(1, 6)

if rule == "udda":
    computer_result = computer % 2
    player_result = player % 2
    if computer_result == player_result:
        print(f"Computer: {computer}, Player: {player}, It's a draw")
    elif computer_result:
        print(f"Computer: {computer}, Player: {player}, Computer wins")
    else:
        print(f"Computer: {computer}, Player: {player}, Player wins")
if rule == "jämnt":
    computer_result = computer % 2
    player_result = player % 2
    if computer_result == player_result:
        print(f"Computer: {computer}, Player: {player}, It's a draw")
    elif computer_result:
        print(f"Computer: {computer}, Player: {player}, Player wins")
    else:
        print(f"Computer: {computer}, Player: {player}, Computer wins")
