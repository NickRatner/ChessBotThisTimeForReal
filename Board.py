from Bishop import Bishop
from King import King
from Knight import Knight
from Pawn import Pawn
from Queen import Queen
from Rook import Rook
import sys
import random
import copy
from UtilityFunctions import UtilityFunctions

class Board:

    def __init__(self):
        self.board = [[Rook("Black"), Knight("Black"), Bishop("Black"), Queen("Black"), King("Black"), Bishop("Black"), Knight("Black"), Rook("Black")],
                          [Pawn("Black"), Pawn("Black"), Pawn("Black"), Pawn("Black"), Pawn("Black"), Pawn("Black"), Pawn("Black"), Pawn("Black")],
                          [None, None, None, None, None, None, None, None],
                          [None, None, None, None, None, None, None, None],
                          [None, None, None, None, None, None, None, None],
                          [None, None, None, None, None, None, None, None],
                          [Pawn("White"), Pawn("White"), Pawn("White"), Pawn("White"), Pawn("White"), Pawn("White"), Pawn("White"), Pawn("White")],
                          [Rook("White"), Knight("White"), Bishop("White"), Queen("White"), King("White"), Bishop("White"), Knight("White"), Rook("White")]
                      ]


    def makeMove(self, oldX, oldY, newX, newY):
        self.board[newY][newX] = self.board[oldY][oldX]
        self.board[newY][newX].hasMoved = True
        self.board[oldY][oldX] = None

        # Pawn promotion
        if str(type(self.board[newY][newX])) == "<class 'Pawn.Pawn'>":
            if newY == 0 and self.board[newY][newX].team == "White":
                self.board[newY][newX] = Queen("White")

            elif newY == 7 and self.board[newY][newX].team == "Black":
                self.board[newY][newX] = Queen("Black")




    def findRandomBlackMove(self):  # this function returns a random move for black (mostly for testing)
        # represented as: [(oldX,oldY), (newX,newY)] where old is the coordinate to move the piece from, and new is the coordinaate to move to

        movableBlackPieces = 0

        for i in range(8):
            for j in range(8):
                if self.board[j][i] and self.board[j][i].team == "Black" and (self.board[j][i].availableMoves(i,j,self.board) != [] or self.board[j][i].availableCaptures(i,j,self.board) != []):
                    movableBlackPieces += 1

        if movableBlackPieces == 0: #this is checkmate, white wins
            sys.exit()

        pieceToMove = random.randint(1, movableBlackPieces)
        pieceCounter = 0

        for i in range(8):
            for j in range(8):
                if self.board[j][i] and self.board[j][i].team == "Black" and (self.board[j][i].availableMoves(i,j,self.board) != [] or self.board[j][i].availableCaptures(i,j,self.board) != []):
                    pieceCounter += 1
                    if pieceCounter == pieceToMove:
                        possibleMoves = self.board[j][i].availableMoves(i,j,self.board) + self.board[j][i].availableCaptures(i,j,self.board)
                        moveToChose = random.randint(0, len(possibleMoves) - 1)
                        oldX = i
                        oldY = j
                        newX = possibleMoves[moveToChose][0]
                        newY = possibleMoves[moveToChose][1]

        return [(oldX,oldY), (newX,newY)]


    def evaluate(self):  # returns a integer representing the current winning team and by how much (positive = white is winning, negative = black is winning)

        values = {"<class 'Pawn.Pawn'>": 1,
                  "<class 'Knight.Knight'>": 3,
                  "<class 'Bishop.Bishop'>": 3,
                  "<class 'Rook.Rook'>": 5,
                  "<class 'Queen.Queen'>": 9,
                  "<class 'King.King'>": 100}  # might remove king, but moves the gurantee king capture (I.E checkmate) are optimal
        currentState = 0

        for i in range(8):
            for j in range(8):
                if self.board[j][i]:
                    if self.board[j][i].team == "White":
                        currentState += values[str(type(self.board[j][i]))]
                    elif self.board[j][i].team == "Black":
                        currentState -= values[str(type(self.board[j][i]))]

        if UtilityFunctions.isCheckMate(self.board, "White"):
            currentState -= 200
        elif UtilityFunctions.isCheckMate(self.board, "Black"):
            currentState += 200

        return currentState



    def findBestBlackMove(self):  # this function returns the best move for black (looking only 1 move ahead)
        # represented as: [(oldX,oldY), (newX,newY)] where old is the coordinate to move the piece from, and new is the coordinaate to move to

        minEvalutaion = self.evaluate()
        oldX = None
        oldY = None
        newX = None
        newY = None


        for i in range(8):
            for j in range(8):
                if self.board[j][i] and self.board[j][i].team == "Black":
                    for move in (self.board[j][i].availableMoves(i, j, self.board) + self.board[j][i].availableCaptures(i, j, self.board)):
                        tempBoard = Board()
                        tempBoard.board = copy.deepcopy(self.board)
                        tempBoard.makeMove(i, j, move[0], move[1])

                        if tempBoard.evaluate() <= minEvalutaion:
                            minEvalutaion = tempBoard.evaluate()
                            oldX = i
                            oldY = j
                            newX = move[0]
                            newY = move[1]

        if oldX == None: # this is checkmate, white wins
                sys.exit()

        return [(oldX,oldY), (newX,newY)]



    def minimax(self, maximizingPlayer, depth, alpha, beta):

        oldX = 0
        oldY = 0
        newX = 0
        newY = 0

        if depth == 0 or UtilityFunctions.isStaleMate(self.board, "White") or UtilityFunctions.isStaleMate(self.board, "Black") or UtilityFunctions.isCheckMate(self.board, "White") or UtilityFunctions.isCheckMate(self.board, "Black"):
            return (self.evaluate(), oldX, oldY, newX, newY)

        if maximizingPlayer: #maximizing player is white, so it is white's turn
            maxEval = -200 #evaluation cannot naturally be lower

            for i in range(8):
                for j in range(8):
                    if self.board[j][i] and self.board[j][i].team == "White":
                        for move in (self.board[j][i].availableMoves(i,j, self.board) + self.board[j][i].availableCaptures(i,j, self.board)): #for all possible white moves find their evaluation
                            tempBoard = Board() #copy the current board, make the move, and test its evaluation
                            tempBoard.board = copy.deepcopy(self.board)
                            tempBoard.makeMove(i, j, move[0], move[1])

                            eval = tempBoard.minimax(False, depth - 1, alpha, beta)[0]
                            if eval > maxEval:
                                oldX = i
                                oldY = j
                                newX = move[0]
                                newY = move[1]

                                maxEval = eval #set the max possible evaluation to the max of the current evaluation, and the newly found one

                            alpha = max(alpha, eval) #alpha is the larger value out of itself and eval, meaning its the highest value white can achieve
                            if beta <= alpha: #if beta (black's best score) is less than alpha (white's best score) we don't need to keep searching since white won't pick this path
                                break
            return (maxEval, oldX, oldY, newX, newY)


        else: #it is the minimizing player, so black's turn
            minEval = 200 #evaluation cannot naturally be higher

            for i in range(8):
                for j in range(8):
                    if self.board[j][i] and self.board[j][i].team == "Black":
                        for move in (self.board[j][i].availableMoves(i,j, self.board) + self.board[j][i].availableCaptures(i,j, self.board)): #for all possible white moves find their evaluation
                            tempBoard = Board() #copy the current board, make the move, and test its evaluation
                            tempBoard.board = copy.deepcopy(self.board)
                            tempBoard.makeMove(i, j, move[0], move[1])

                            eval = tempBoard.minimax(True, depth - 1, alpha, beta)[0]
                            if eval < minEval:
                                oldX = i
                                oldY = j
                                newX = move[0]
                                newY = move[1]

                                minEval = eval #set the max possible evaluation to the max of the current evaluation, and the newly found one

                            if eval == minEval and random.randint(1,5) == 1: #both moves have the same evaluation
                                oldX = i
                                oldY = j
                                newX = move[0]
                                newY = move[1]

                                minEval = eval  # set the max possible evaluation to the max of the current evaluation, and the newly found one

                            beta = min(beta, eval)  # beta is the smaller value out of itself and eval, meaning its the lowest value black can achieve
                            if beta <= alpha:
                                break
            return (minEval, oldX, oldY, newX, newY)