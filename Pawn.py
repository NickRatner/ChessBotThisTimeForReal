from Piece import Piece
from UtilityFunctions import UtilityFunctions

class Pawn(Piece):


    def availableMoves(self, currentX, currentY, board, mode = 0):
        # mode argument determines if this function should account for moves the put the king in check
        # when run with mode = 0, it does account for this. This is used in the main loop when deciding where a piece can move
        # mode = 1 is for simply finding all of a pieces possible moves.

        availableMoves = []

        if self.team == "White":
            if not self.outOfBounds(currentX, currentY - 1) and board[currentY - 1][currentX] == None:
                availableMoves.append((currentX, currentY - 1))

            if not self.hasMoved:
                if board[currentY - 1][currentX] == None and board[currentY - 2][currentX] == None:
                    availableMoves.append((currentX, currentY - 2))

        else: #if team == "Black"
            if not self.outOfBounds(currentX, currentY + 1) and board[currentY + 1][currentX] == None:
                availableMoves.append((currentX, currentY + 1))

            if not self.hasMoved:
                if board[currentY + 1][currentX] == None and board[currentY + 2][currentX] == None:
                    availableMoves.append((currentX, currentY + 2))


        if mode == 0:
            if self.isPieceBlockingCheck(currentX, currentY, board) or UtilityFunctions.isInCheck(board, self.team):  # if the piece is not blocking check, it can move freely, otherwise must test its moves
                return self.filterBadMoves(availableMoves, currentX, currentY, board)

        return availableMoves


    def availableCaptures(self, currentX, currentY, board, mode = 0):
        # mode argument determines if this function should account for moves the put the king in check
        # when run with mode = 0, it does account for this. This is used in the main loop when deciding where a piece can move
        # mode = 1 is for simply finding all of a pieces possible moves.

        availableCaptures = []

        if self.team == "White":
            if not Piece.outOfBounds(currentX - 1, currentY - 1) and board[currentY - 1][currentX - 1]: #checks if the possible capture spot is in bounds, and contains a piece

                if board[currentY - 1][currentX - 1].team == "Black": #checks if thats piece's team is "Black"
                    availableCaptures.append((currentX - 1, currentY - 1))

            if not Piece.outOfBounds(currentX + 1,currentY - 1) and board[currentY - 1][currentX + 1]: #checks if the possible capture spot is in bounds, and contains a piece
                if board[currentY - 1][currentX + 1].team == "Black": #checks if thats piece's team is "Black"
                    availableCaptures.append((currentX + 1, currentY - 1))

        else: #if the piece's team is "Black"
            if not Piece.outOfBounds(currentX - 1, currentY + 1) and board[currentY + 1][currentX - 1]:  # checks if the possible capture spot is in bounds, and contains a piece
                if board[currentY + 1][currentX - 1].team == "White":  # checks if thats piece's team is "White"
                    availableCaptures.append((currentX - 1, currentY + 1))

            if not Piece.outOfBounds(currentX + 1, currentY + 1) and board[currentY + 1][currentX + 1]:  # checks if the possible capture spot is in bounds, and contains a piece
                if board[currentY + 1][currentX + 1].team == "White":  # checks if thats piece's team is "White"
                    availableCaptures.append((currentX + 1, currentY + 1))


        if mode == 0:
            if self.isPieceBlockingCheck(currentX, currentY, board) or UtilityFunctions.isInCheck(board, self.team):  # if the piece is not blocking check, it can move freely, otherwise must test its moves
                return self.filterBadMoves(availableCaptures, currentX, currentY, board)

        return availableCaptures