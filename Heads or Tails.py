import random

play_again = "y"
while play_again == "y":

        print("Choose heads or tails")
        choice = input()
        print(f"You chose {choice}")

        computer_flip = random.choice(["heads", "tails"])
        if computer_flip == choice:
            print("You win, I flipped", computer_flip, "!")
        else:
            print("You lose, I flipped", computer_flip, "!")

        print("Play again? (press enter to continue and escape to quit)")
        play_again = input()
        if play_again != "y":
            break