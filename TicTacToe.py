board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

currentPlayer = "X"
winner = None
exitPromptPrinted = False

gameState = 0   #GameState tracker [0 = pre game, 1 = ongoing game, 2 = post game, 3 = exit application]

import random; import keyboard; import time

def drawBoard(board):       #---- Draw game state
    print("-------------")
    print("| " + board[0] + " | " + board[1] + " | " + board[2] + " |")
    print("-------------")
    print("| " + board[3] + " | " + board[4] + " | " + board[5] + " |")
    print("-------------")
    print("| " + board[6] + " | " + board[7] + " | " + board[8] + " |")
    print("-------------")

def playerInput(board):     #---- Player input
    _input = int(input("Enter a number 1-9: "))
    if(_input >= 1 and _input <= 9 and board[_input-1] == "-"):
        board[_input-1] = currentPlayer
    else:
        print("Invalid input, too bad!")    

def exitPrompt():
    global exitPromptPrinted
    exitPromptPrinted = True
    print("Press ENTER or ESC to quit application")

def exitInput():
    global gameState
    if keyboard.is_pressed('enter') | keyboard.is_pressed('esc'):
        gameState = 3

def checkHorizontal(board):     #---- Check win/lose/tie conditions
    global winner
    if(board[0] == board[1] == board[2] and board[0] != "-"):
        winner = board[0]
        return True
    elif(board[3] == board[4] == board[5] and board[3] != "-"):
        winner = board[3]
        return True
    elif(board[6] == board[7] == board[8] and board[6] != "-"):
        winner = board[6]
        return True

def checkVertical(board):
    global winner
    if(board[0] == board[3] == board[6] and board[0] != "-"):
        winner = board[0]
        return True
    elif(board[1] == board[4] == board[7] and board[1] != "-"):
        winner = board[1]
        return True
    elif(board[2] == board[5] == board[8] and board[2] != "-"):
        winner = board[2]
        return True
      
def checkDiagonal(board):
    global winner
    if(board[0] == board[4] == board[8] and board[0] != "-"):
        winner = board[0]
        return True
    elif(board[2] == board[4] == board[6] and board[2] != "-"):
        winner = board[2]
        return True

def checkWinConditions():
    if(checkDiagonal(board) or checkHorizontal(board) or checkVertical(board)):
        global gameState        
        print(f"{winner} is victorious!")      
        gameState = 2
    elif("-") not in board:                
        print("Tied!")  
        gameState = 2     

def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

def bot(board): 
    while(currentPlayer == "O"):
            position = random.randint(0,8)
            if(board[position] == "-"):     
                time.sleep(random.uniform(0.75,1.5))
                board[position] = currentPlayer
                print("Opponent chose position " + str(position))
                switchPlayer()      
           
while(gameState <= 2):
    if(gameState == 0):
        print("Welcome to Tic Tac Toe!")
        gameState = 1
    elif(gameState == 1):
        drawBoard(board)
        playerInput(board)  
        drawBoard(board)
        checkWinConditions()
        switchPlayer()
        bot(board)
        checkWinConditions()
    elif(gameState == 2):        
        exitPrompt() if not exitPromptPrinted else None
        exitInput()     
