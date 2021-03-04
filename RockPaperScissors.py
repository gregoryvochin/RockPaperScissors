import random

options = ("rock", "paper", "scissors")

rounds = 0

print("Welcome to Gregory's \"Rock, Paper, Scissors\" simulator!\n")

while (rounds <= 0):

    rounds = input("Enter the number of rounds you would like to execute: ")

    if rounds.isdigit():

        rounds = int(rounds)

        if rounds > 9:
            rounds = -1
            print("Please enter a number less than 9")
        else:
            break

else:
    print("Please enter an number greater than 0")

print("You have chosen", rounds, "round(s).")

roundCount = 0
drawCount = 0
compWins = 0
userWins = 0 

while roundCount < rounds:

    userInput = input("\nEnter rock, paper, or scissors to start: ")

    userInput = userInput.lower()

    if userInput in options:
        print("\nYou chose: " + userInput)

        i = random.randrange(0,3)

        computerMove = options[i]

        print("The computer chose: " + computerMove)

        if userInput == computerMove:
            print("It's a draw!")
            drawCount += 1
        elif userInput == "rock" and computerMove == "scissors":
            print("You win!")
            userWins += 1
        elif userInput == "rock" and computerMove == "paper":
            print("You lose!")
            compWins += 1
        elif userInput == "paper" and computerMove == "rock":
            print("You win!")
            userWins += 1
        elif userInput == "paper" and computerMove == "scissors":
            print("You lose!")
            compWins += 1
        elif userInput == "scissors" and computerMove == "paper":
            print("You win!")
            userWins += 1
        elif userInput == "scissors" and computerMove == "rock":
            print("You lose!")
            compWins += 1
        else:
            print("uhh...")

        roundCount += 1
        
    else:
        print("please enter a valid option of rock, paper, or scissors.")    
    
else:
    print("\nGame Over!")

    if compWins > userWins:
        print("You lose!")
    elif compWins < userWins:
        print("You win!")
    elif compWins == userWins:
        print("It's a draw!")
    else:
        print("uhh...")

    print("The score ended at", userWins, "-", compWins, "with", drawCount, "draws!")
