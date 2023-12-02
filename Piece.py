from UtilityFunctions import UtilityFunctions
import copy

class Piece:

    def __init__(self, team):
        self.team = team #White or Black
        self.hasMoved = False

    @staticmethod
    def outOfBounds(x, y):
        return x < 0 or x > 7 or y < 0 or y > 7


    def isPieceBlockingCheck(self, x, y, board):
        #given a board, and a coordinate, is the piece at that coordinate blocking check for its king (if not, all its moves are safe)
        #note: returns true if this piece is single-handedly preventing check, meaning even if it is blocking check, but the king is in check anyway, this returns false

        # finds the piece
        piece = board[y][x]

        if UtilityFunctions.isInCheck(board, piece.team):
            return False

        #if the piece didn't exist, would the king be in check? if yes, the piece is block check
        tempBoard = [row[:] for row in board]
        tempBoard[y][x] = None

        return UtilityFunctions.isInCheck(tempBoard, piece.team)


    def filterBadMoves(self, moves, x, y, board):
        finalMoves = moves.copy()
        tempBoard = copy.deepcopy(board)
        for move in moves:
            # move the piece to it's new position and confirm if king is in check
            tempBoard[move[1]][move[0]] = self
            tempBoard[y][x] = None

            if UtilityFunctions.isInCheck(tempBoard, self.team):  # if the move puts your king in check, remove it from available moves
                finalMoves.remove(move)

            tempBoard = copy.deepcopy(board)

        return finalMoves