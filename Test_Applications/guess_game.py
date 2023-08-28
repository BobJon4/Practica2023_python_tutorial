correct_guess = 4
tries = 3

guess = int(input("Guess: "))
tries -= 1

while guess != correct_guess and tries:
    guess = int(input("Guess: "))
    tries -= 1

if tries == 0:
    print("Game Over")

if tries > 0:
    print("Correct")