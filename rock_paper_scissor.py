import random

print("| **** Rock Paper Scissor ****|")

def play_game(userCh):
    list = ["R", "P", "S"]
    userScore = 0
    computerScore = 0
    i = 1
    while True:
        computerCh = str(random.choice(list))
        if userCh == computerCh:
            print("Tie You Both Entered Same")
        elif userCh == "R":
            print("Computer Enter: ", computerCh)
            if computerCh == "P":
                print("You lose! Paper covers Rock")
                computerScore += 1
            else:
                print("You win! Rock smashes Scissors")
                userScore += 1
        elif userCh == "P":
            print("Computer Enter: ", computerCh)
            if computerCh == "S":
                print("You lose! Scissor cut Paper")
                computerScore += 1
            else:
                print("You win! Paper covers Rock")
                userScore += 1
        elif userCh == "S":
            print("Computer Enter: ", computerCh)
            if computerCh == "R":
                print("You lose! Rock smashes Scissors")
                computerScore += 1
            else:
                print("You win! Scissor cut Paper")
                userScore += 1
        else:
            print(":(")
        play_again = input("Play again? (y/n): ")
        if play_again.lower() != "y":
         break

        print("\n\t******ScoreBoard******")
        print(f"\t You: {userScore} | Computer: {computerScore}")
        print("\t**** Rock Paper Scissor ****|")
        print(f"Game No:[{i}]")
        print("==============")
        i += 1
       
userCh = input("Enter Rock, Paper, Scissors (key to press: R,P,S): ").upper()
play_game(userCh)
