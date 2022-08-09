import random

print("\t**** Tic Tac Toe ****|")

possibleNumbers = [1,2,3,4,5,6,7,8,9]
gameBoard = [[1,2,3], [4,5,6], [7,8,9]]
row = 3
col = 3

def print_game_board():
  for x in range(row):
    print("\n+---+---+---+")
    print("|", end="")
    for y in range(col):
      print("", gameBoard[x][y], end=" |")
  print("\n+---+---+---+")

def modifyArray(num, turn):
  num -= 1
  if(num == 0):
    gameBoard[0][0] = turn
  elif(num == 1):
    gameBoard[0][1] = turn
  elif(num == 2):
    gameBoard[0][2] = turn
  elif(num == 3):
    gameBoard[1][0] = turn
  elif(num == 4):
    gameBoard[1][1] = turn
  elif(num == 5):
    gameBoard[1][2] = turn
  elif(num == 6):
    gameBoard[2][0] = turn
  elif(num == 7):
    gameBoard[2][1] = turn
  elif(num == 8):
    gameBoard[2][2] = turn

# check for a winner
def checkForWinner(gameBoard):
  
  # Vertical Check 
  if(gameBoard[0][0] == 'X' and gameBoard[0][1] == 'X' and gameBoard[0][2] == 'X'):
    print("X has won!")
    return "X"
  elif(gameBoard[0][0] == 'O' and gameBoard[0][1] == 'O' and gameBoard[0][2] == 'O'):
    print("O has won!")
    return "O"
  elif(gameBoard[1][0] == 'X' and gameBoard[1][1] == 'X' and gameBoard[1][2] == 'X'):
    print("X has won!")
    return "X"
  elif(gameBoard[1][0] == 'O' and gameBoard[1][1] == 'O' and gameBoard[1][2] == 'O'):
    print("O has won!")
    return "O"
  elif(gameBoard[2][0] == 'X' and gameBoard[2][1] == 'X' and gameBoard[2][2] == 'X'):
    print("X has won!")
    return "X"
  elif(gameBoard[2][0] == 'O' and gameBoard[2][1] == 'O' and gameBoard[2][2] == 'O'):
    print("O has won!")
    return "O"
  
  #Horizontal Check
  if(gameBoard[0][0] == 'X' and gameBoard[1][0] == 'X' and gameBoard[2][0] == 'X'):
    print("X has won!")
    return "X"
  elif(gameBoard[0][0] == 'O' and gameBoard[1][0] == 'O' and gameBoard[2][0] == 'O'):
    print("O has won!")
    return "O"
  elif(gameBoard[0][1] == 'X' and gameBoard[1][1] == 'X' and gameBoard[2][1] == 'X'):
    print("X has won!")
    return "X"
  elif(gameBoard[0][1] == 'O' and gameBoard[1][1] == 'O' and gameBoard[2][1] == 'O'):
    print("O has won!")
    return "O"
  elif(gameBoard[0][2] == 'X' and gameBoard[1][2] == 'X' and gameBoard[2][2] == 'X'):
    print("X has won!")
    return "X"
  elif(gameBoard[0][2] == 'O' and gameBoard[1][2] == 'O' and gameBoard[2][2] == 'O'):
    print("O has won!")
    return "O"
  
  #cross X check
  elif(gameBoard[0][0] == 'X' and gameBoard[1][1] == 'X' and gameBoard[2][2] == 'X'):
    print("X has won!")
    return "X"
  elif(gameBoard[0][0] == 'O' and gameBoard[1][1] == 'O' and gameBoard[2][2] == 'O'):
    print("O has won!")  
    return "O"
  elif(gameBoard[0][2] == 'X' and gameBoard[1][1] == 'X' and gameBoard[2][0] == 'X'):
    print("X has won!")  
    return "X"
  elif(gameBoard[0][2] == 'O' and gameBoard[1][1] == 'O' and gameBoard[2][0] == 'O'):
    print("O has won!") 
    return "O" 
  else:
    return "N"

loop = False
turnCounter = 0

while(loop == False):


  if(turnCounter % 2 == 0):
    print_game_board()
    numberPicked = int(input("\nChoose a number [1-9]: "))
    if(numberPicked >= 1 or numberPicked <= 9):
      modifyArray(numberPicked, 'X')
      possibleNumbers.remove(numberPicked)
    else:
      print("Invalid input. Please try again.")
    turnCounter += 1
    

  else:
    while(True):
      computer = random.choice(possibleNumbers)
      print("\n Computer choice: ", computer)
      if(computer in possibleNumbers):
        modifyArray(computer, 'O')
        possibleNumbers.remove(computer)
        turnCounter += 1
        break
  
  winner = checkForWinner(gameBoard)
  if(winner != "N"):
   print("\t**** Tic Tac Toe ****|")
   break
