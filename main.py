import pygame
import Board
from UtilityFunctions import UtilityFunctions
from Rook import Rook
from King import King

chessBoard = Board.Board()

def drawBoard(gameWindow):

    pygame.draw.rect(gameWindow, (193, 75, 31), (0, 0, 800, 800))  # draws the chess board background

    for i in range(8):  # this loop draws all the light colored rectangles on the board
        for j in range(8):
            if i % 2 == 0:
                if j % 2 == 0:
                    pygame.draw.rect(gameWindow, (225, 198, 153), (j * 100, i * 100, 100, 100))
            elif i % 2 != 0:
                if j % 2 != 0:
                    pygame.draw.rect(gameWindow, (225, 198, 153), (j * 100, i * 100, 100, 100))

    for i in range(8):  # this loop draws all the chess pieces
        for j in range(8):
            if chessBoard.board[i][j]:

                image = pygame.image.load("Images/" + str(chessBoard.board[i][j].team) + chessBoard.board[i][j].__class__.__name__ + "Icon-rbg.png")
                gameWindow.blit(image, (j * 100, i * 100))


def drawAvailableMoves(piece): #takes in a coordinate, and displays the available moves of the piece

    for i in range(8):
        for j in range(8):
            if chessBoard.board[i][j] == piece:
                x = j
                y = i
                break

    greenCircleImage = pygame.image.load("Images/greenCircle-rbg.png")
    redCircleImage = pygame.image.load("Images/redCircle-rbg.png")

    for location in chessBoard.board[y][x].availableMoves(x,y, chessBoard.board):  # This will return a list of all coordinates where a move is possible
        gameWindow.blit(greenCircleImage, (location[0] * 100, location[1] * 100))

    for location in chessBoard.board[y][x].availableCaptures(x,y, chessBoard.board):  # This will return a list of all coordinates where a capture is possible
        gameWindow.blit(redCircleImage, (location[0] * 100, location[1] * 100))



gameWindow = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Chess Bot")


pieceSelected = False
chosenPiece = None
previousPiece = None
previousMX = 0
previousMY = 0
playerMoved = False

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN: #when player clicks
            mx, my = pygame.mouse.get_pos()

            if chessBoard.board[int(my / 100)][int(mx / 100)]: #if the square clicked on contains a piece
                chosenPiece = chessBoard.board[int(my / 100)][int(mx / 100)]

                if pieceSelected or chosenPiece.team == "White": #ensures the player can only interact with white piece, assuming a white piece isn't already selected

                    if pieceSelected: #if a piece is currently selected

                        #if a piece is selected, and another one was clicked on that is within the selected piece's available captures, capture the piece
                        if (int(mx / 100), int(my / 100)) in chessBoard.board[int(previousMY / 100)][int(previousMX / 100)].availableCaptures(int(previousMX / 100), int(previousMY / 100), chessBoard.board):
                            chessBoard.board[int(previousMY / 100)][int(previousMX / 100)].hasMoved = True
                            chessBoard.board[int(my / 100)][int(mx / 100)] = chessBoard.board[int(previousMY / 100)][int(previousMX / 100)]  # update the new position
                            chessBoard.board[int(previousMY / 100)][int(previousMX / 100)] = None  # clear the old position
                            playerMoved = True

                            pieceSelected = False

                        elif chosenPiece == chessBoard.board[int(previousMY / 100)][int(previousMX / 100)]: #the selected piece is the same as the one currently clicked on
                            pieceSelected = False
                            chosenPiece = None

                        else: #a new piece is selected
                            pieceSelected = True


                    else: #if a piece was not currently selected, select the piece
                        pieceSelected = True

            else: #if the square selected does not contain a piece, reset the selected piece

                if pieceSelected and chosenPiece:
                    # castling
                    if str(type(chosenPiece)) == "<class 'King.King'>" and not chosenPiece.hasMoved:
                        if (int(mx / 100), int(my / 100)) == (2, 7):  # white king castle left
                            chessBoard.board[7][3] = Rook("White") #move the rook
                            chessBoard.board[7][3].hasMoved = True
                            chessBoard.board[7][0] = None
                            chessBoard.board[7][2] = King("White")  # move the king
                            chessBoard.board[7][2].hasMoved = True
                            chessBoard.board[7][4] = None
                            playerMoved = True

                        elif (int(mx / 100), int(my / 100)) == (6, 7):  # white king castle right
                            chessBoard.board[7][5] = Rook("White") #move the rook
                            chessBoard.board[7][5].hasMoved = True
                            chessBoard.board[7][7] = None
                            chessBoard.board[7][6] = King("White")  # move the king
                            chessBoard.board[7][6].hasMoved = True
                            chessBoard.board[7][4] = None
                            playerMoved = True

                        elif (int(mx / 100), int(my / 100)) == (2, 0):  # black king castle left
                            chessBoard.board[0][3] = Rook("Black") #move the rook
                            chessBoard.board[0][3].hasMoved = True
                            chessBoard.board[0][0] = None
                            chessBoard.board[0][2] = King("Black")  # move the king
                            chessBoard.board[0][2].hasMoved = True
                            chessBoard.board[0][4] = None
                            playerMoved = True

                        elif (int(mx / 100), int(my / 100)) == (6, 0):  # black king castle right
                            chessBoard.board[0][5] = Rook("Black") #move the rook
                            chessBoard.board[0][5].hasMoved = True
                            chessBoard.board[0][7] = None
                            chessBoard.board[0][6] = King("Black")  # move the king
                            chessBoard.board[0][6].hasMoved = True
                            chessBoard.board[0][4] = None
                            playerMoved = True

                    # if a piece was selected, and the click was on one of its avaialbe moves, move the piece
                    if (int(mx / 100), int(my / 100)) in chosenPiece.availableMoves(int(previousMX / 100), int(previousMY / 100), chessBoard.board):
                        chosenPiece.hasMoved = True
                        chessBoard.board[int(my / 100)][int(mx / 100)] = chosenPiece #update the new position
                        chessBoard.board[int(previousMY / 100)][int(previousMX / 100)] = None #clear the old position
                        playerMoved = True


                pieceSelected = False

            if UtilityFunctions.isCheckMate(chessBoard.board, "Black"): #checks for checkmate after each moves, and ends the game
                print("Game Over: White Wins")

            if playerMoved:
                playerMoved = False
                # computer makes move here
                [(oldX,oldY), (newX,newY)] = UtilityFunctions.findRandomBlackMove(chessBoard.board)
                chessBoard.board[newY][newX] = chessBoard.board[oldY][oldX]
                chessBoard.board[oldY][oldX] = None



            if UtilityFunctions.isCheckMate(chessBoard.board, "White"): #checks for checkmate after each moves, and ends the game
                print("Game Over: Black Wins")


            previousMX = mx
            previousMY = my


    # Drawing code goes here
    drawBoard(gameWindow)

    if pieceSelected:
        drawAvailableMoves(chosenPiece)

    # Update display
    pygame.display.update()  #update all visuals

pygame.display.quit()
