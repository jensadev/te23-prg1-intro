# # bestäm om det är udda eller jämnt
# # rulla tärningar
# # vinnaren är det som bestämts
# from random import randint

# rule = input("Skriv om ni spelar udda eller jämnt:")
# computer = randint(1, 6)
# player = randint(1, 6)

# if rule == "udda":
#     # logiken för att bestämma vinnare om det är udda
#     computer_result = computer % 2
#     player_result = player % 2
#     # if computer or player result is 0, number is even
#     print(
#         f"Datorn rullade {computer_result} och spelaren {player_result}, spelregeln var {rule}"
#     )
# else:
#     computer_result = computer % 2
#     player_result = player % 2
#     # if computer or player result is 1, number is odd
#     print(
#         f"Datorn rullade {computer_result} och spelaren {player_result}, spelregeln var {rule}"
#    )

from random import randint

rule = input("Skriv om ni spelar udda eller jämnt:")
computer = randint(1, 6)
player = randint(1, 6)
odd = (1, 3, 5)
even = (2, 4, 6)
if rule == "udda":
    computer_result = computer in odd
    player_result = player in odd
    if computer_result == player_result:
        print(f"Computer: {computer}, Player: {player}, It's a draw")
    elif computer_result:
        print(f"Computer: {computer}, Player: {player}, Computer wins")
    else:
        print(f"Computer: {computer}, Player: {player}, Player wins")
