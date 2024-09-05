# bestäm om det är udda eller jämnt
# rulla tärningar
# vinnaren är det som bestämts
from random import randint

rule = input("Skriv om ni spelar udda eller jämnt:")
computer = randint(1, 6)
player = randint(1, 6)

if rule == "udda":
    # logiken för att bestämma vinnare om det är udda
    computer_result = computer % 2
    player_result = player % 2
    # if computer or player result is 0, number is even
    print(
        f"Datorn rullade {computer_result} och spelaren {player_result}, spelregeln var {rule}"
    )
else:
    computer_result = computer % 2
    player_result = player % 2
    # if computer or player result is 1, number is odd
    print(
        f"Datorn rullade {computer_result} och spelaren {player_result}, spelregeln var {rule}"
    )
