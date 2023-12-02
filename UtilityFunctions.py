import random
import sys

class UtilityFunctions:

    @staticmethod
    def isInCheck(board, team):

        #finds the coordinates of the king
        for i in range(8):
            for j in range(8):
                if str(type(board[j][i])) == "<class 'King.King'>":
                    if board[j][i].team == team:
                        kingX = i
                        kingY = j
                        break

        #note, kingX and kingY may not be set, but only if there is no king found, which should never be the case

        #checks availableCaptures() of all pieces on the other team
        for i in range(8):
            for j in range(8):
                if board[j][i] and board[j][i].team != team: #if there is a piece at the current square, and they are the opposite team of the king
                    if (kingX, kingY) in board[j][i].availableCaptures(i, j, board, mode=1):
                        return True

        return False

    @staticmethod
    def isCheckMate(board, team): #returns if the given team is in checkmate

        if not UtilityFunctions.isInCheck(board,team):
            return False

        for i in range(8):
            for j in range(8):
                if board[j][i] and board[j][i].team == team:  # if we reach a piece on the same team as the king check its availble moves
                    if not board[j][i].availableCaptures(i, j, board) == [] or not board[j][i].availableMoves(i, j, board) == []:
                        return False

        return True

    @staticmethod
    def isStaleMate(board, team):

        if UtilityFunctions.isInCheck(board, team):
            return False

        #if pieces have no available moves and are not in check
        for i in range(8):
            for j in range(8):
                if board[j][i] and board[j][i].team == team:  # if we reach a piece on the same team as the king check its availble moves
                    if not board[j][i].availableCaptures(i, j, board) == [] or not board[j][i].availableMoves(i, j, board) == []:
                        return False #if a piece can move, the team is not in stalemate

        return True



    @staticmethod
    def findRandomBlackMove(board):  # this function returns a random move for black (mostly for testing)
        # represented as: [(oldX,oldY), (newX,newY)] where old is the coordinate to move the piece from, and new is the coordinaate to move to

        movableBlackPieces = 0

        for i in range(8):
            for j in range(8):
                if board[j][i] and board[j][i].team == "Black" and (board[j][i].availableMoves(i,j,board) != [] or board[j][i].availableCaptures(i,j,board) != []):
                    movableBlackPieces += 1

        if movableBlackPieces == 0: #this is checkmate, white wins
            sys.exit()

        pieceToMove = random.randint(1, movableBlackPieces)
        pieceCounter = 0

        for i in range(8):
            for j in range(8):
                if board[j][i] and board[j][i].team == "Black" and (board[j][i].availableMoves(i,j,board) != [] or board[j][i].availableCaptures(i,j,board) != []):
                    pieceCounter += 1
                    if pieceCounter == pieceToMove:
                        possibleMoves = board[j][i].availableMoves(i,j,board) + board[j][i].availableCaptures(i,j,board)
                        moveToChose = random.randint(0, len(possibleMoves) - 1)
                        oldX = i
                        oldY = j
                        newX = possibleMoves[moveToChose][0]
                        newY = possibleMoves[moveToChose][1]

        return [(oldX,oldY), (newX,newY)]


    @staticmethod
    def evaluate(board): #returns a integer representing the current winning team and by how much (positive = white is winning, negative = black is winning)

        values = {"<class 'Pawn.Pawn'>" : 1,
                  "<class 'Knight.Knight'>" : 3,
                  "<class 'Bishop.Bishop'>" : 3,
                  "<class 'Rook.Rook'>" : 5,
                  "<class 'Queen.Queen'>" : 9,
                  "<class 'King.King'>": 100} #might remove king, but moves the gurantee king capture (I.E checkmate) are optimal
        currentState = 0

        for i in range(8):
            for j in range(8):
                if board[j][i]:
                    if board[j][i].team == "White":
                        currentState += values[str(type(board[j][i]))]
                    elif board[j][i].team == "Black":
                        currentState -= values[str(type(board[j][i]))]

        if UtilityFunctions.isInCheck(board, "White"):
            currentState += 10
        if UtilityFunctions.isInCheck(board, "Black"):
            currentState -= 10

        return currentState



    @staticmethod
    def findBestBlackMove(board):  # this function returns the best move for black (minimax! woo!)
        # represented as: [(oldX,oldY), (newX,newY)] where old is the coordinate to move the piece from, and new is the coordinaate to move to

        pass