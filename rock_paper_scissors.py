import random

print("==============================")
print("     Rock, Paper, Scissors!")
print("==============================")
print("")

print("Type the number corresponding to rock, paper, or scissors.")
print("1) Rock")
print("2) Paper")
print("3) Scissors")

player = int(input("Which do you choose? "))
computer = random.randint(1, 3)

choices = {1: "rock", 2: "paper", 3: "scissors" }

print("")
print("====================")
if player == 1 and computer == 3:
    print(f"You chose: {choices[player]}")
    print(f"CPU chose: {choices[computer]}")
    print("Player wins!")
elif player == 2 and computer == 1:
    print(f"You chose: {choices[player]}")
    print(f"CPU chose: {choices[computer]}")
    print("Player wins!")
elif player == 3 and computer == 2:
    print(f"You chose: {choices[player]}")
    print(f"CPU chose: {choices[computer]}")
    print("Player wins!")
elif player == computer:
    print(f"You chose: {choices[player]}")
    print(f"CPU chose: {choices[computer]}")
    print("It's a tie!")
else:
    print(f"You chose: {choices[player]}")
    print(f"CPU chose: {choices[computer]}")
    print("CPU wins!")
print("====================")
