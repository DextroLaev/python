import random

def drawBoard(board):
    print('   |    |')
    print(' '+board[7]+' | '+' '+board[8]+' | '+board[9]+' ')
    print('   |    |')
    print('------------')
    print('   |    |')
    print(' '+board[4]+' | '+' '+board[5]+' | '+board[6]+' ')
    print('   |    |')
    print('------------')
    print('   |    |')
    print(' '+board[1]+' | '+' '+board[2]+' | '+board[3]+' ')
    print('   |    |')
    

def inputPlayerLetter():
    letter=''
    while not(letter == 'X' or letter == 'O'):
        print("Do you want to be X or O \n")
        letter = input().upper()
        
    if letter == 'X':
        return ['X','O'] # returns a list, here the fist item is letter for the player and second for computer
    else:
        return ['O','X']

def whoGoesFirst():
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'

def playAgain():
    return input("do you want to play again? y or n").lower().startswith('y')

def makeMove(board, letter, move):  # where move is the position of the board 
    board[move] = letter

def isWinner(bo, le): # true if any of the winning combination  of the board is found

    return ((bo[1] == le and bo[2] == le and bo[3] == le) or
    (bo[4] == le and bo[5] == le and bo[6] == le) or
    (bo[7] == le and bo[8] == le and bo[9] == le) or
    (bo[1] == le and bo[4] == le and bo[7] == le) or
    (bo[2] == le and bo[5] == le and bo[8] == le) or
    (bo[3] == le and bo[6] == le and bo[9] == le) or
    (bo[1] == le and bo[5] == le and bo[9] == le) or
    (bo[3] == le and bo[5] == le and bo[7] == le) )

def getBoardCopy(board):
    dupeBoard=[]

    for i in board:
        dupeBoard.append(i)
    return dupeBoard

def isSpaceFree(board, move):
    return board[move] == ' '

def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print("What is your next move? (1-9)")
        move=input()
    return int(move)

def chooseRandomMovesFromList(board, movesList):
    possibleMoves=[]
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) !=0:
        return random.choice(possibleMoves)
    else:
        return None

#game logic for the computers move selection--------------------------------------------------

def getComputerMove(board, computerLetter):
    if computerLetter=='X':
        playerLetter='O'
    else:
        playerLetter='X'

    for i in range(1, 10):
        copy=getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    move = chooseRandomMovesFromList(board, [1,3,7,9])   # chosing any corner position
    if move != None:
        return move

    if isSpaceFree(board, 5):   #chosing the center position
        return 5

    return chooseRandomMovesFromList(board, [2,4,6,8])   #chosing any posistion form the corner

#-------------------------------------------------------------------------------------------------

def isBoardFull(board):
    for i in range(1,10):
        if isSpaceFree(board, i):
            return False
    return True
   
#--------------------DRIVER SECTION--------------------------------------------------------------

print('Welcome to Tic Tac Toe!')

while True:
    theBoard =[' ']*10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn+' will go first. ')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)
            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('You WON the game')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'
        else:
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)
            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer won')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a Tie!')
                else:
                    turn = 'player'

    if not playAgain():
        break