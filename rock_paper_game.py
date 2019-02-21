# rock, paper, scissors game

# imports
import random

print("-----------The Rock, Paper, Scissors Game-----------")


# main function
def main():
    program_choice = random.randint(1, 3)
    program_play(program_choice)


def program_play(rand_choice):
    # ask for user input
    user_choice = input("Please enter your choice of rock, paper, or scissors? ")

    # assigning names to the number the program chose
    # 1 = rock
    if rand_choice == 1:
        str_program_choice = "rock"
        print("I chose rock")
    # 2 = paper
    elif rand_choice == 2:
        str_program_choice = "paper"
        print("I chose paper")
    # 3 = scissors
    elif rand_choice == 3:
        str_program_choice = "scissors"
        print("I chose scissors")

    game_winner(user_choice, str_program_choice)


# function that determines the winner
def game_winner(user, program):
    # tie outcome
    if user == program:
        print("We must play again to determine the true winner!")
        print("")
        # call on main function to play the game again
        main()
# user picks rock outcome
    elif user == "rock" and program == "paper":
        print("")
        print("You loose, better luck next time!")
    elif user == "rock" and program == "scissors":
        print("")
        print("You win!")
# user picks paper outcome
    elif user == "paper" and program == "rock":
        print("")
        print("You win!")
    elif user == "paper" and program == "scissors":
        print("")
        print("You loose, better luck next time!")
# user picks scissors outcome
    elif user == "scissors" and program == "paper":
        print("")
        print("You win!")
    elif user == "scissors" and program == "rock":
        print("")
        print("You loose, better luck next time!")


# call on main function to start the game
main()

