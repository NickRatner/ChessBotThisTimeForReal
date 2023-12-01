from Piece import Piece
from UtilityFunctions import UtilityFunctions

class Knight(Piece):

    def availableMoves(self, currentX, currentY, board, mode = 0):
        # mode argument determines if this function should account for moves the put the king in check
        # when run with mode = 0, it does account for this. This is used in the main loop when deciding where a piece can move
        # mode = 1 is for simply finding all of a pieces possible moves.

        availableMoves = []

        list1 = [-1, 1]
        list2 = [-2, 2]

        for i in list1:
            for j in list2:
                if not Piece.outOfBounds(currentX + i, currentY + j) and board[currentY + j][currentX + i] == None:
                    availableMoves.append((currentX + i, currentY + j))

        for i in list2:
            for j in list1:
                if not Piece.outOfBounds(currentX + i, currentY + j) and board[currentY + j][currentX + i] == None:
                    availableMoves.append((currentX + i, currentY + j))


        if mode == 0:
            if self.isPieceBlockingCheck(currentX, currentY, board) or UtilityFunctions.isInCheck(board, self.team):  # if the piece is not blocking check, it can move freely, otherwise must test its moves
                return self.filterBadMoves(availableMoves, currentX, currentY, board)

        return availableMoves


    def availableCaptures(self, currentX, currentY, board, mode = 0):
        # mode argument determines if this function should account for moves the put the king in check
        # when run with mode = 0, it does account for this. This is used in the main loop when deciding where a piece can move
        # mode = 1 is for simply finding all of a pieces possible moves.

        availableCaptures = []

        list1 = [-1, 1]
        list2 = [-2, 2]

        for i in list1:
            for j in list2:
                if not Piece.outOfBounds(currentX + i, currentY + j) and board[currentY + j][currentX + i]:
                    if self.team == "White" and board[currentY + j][currentX + i].team == "Black":
                        availableCaptures.append((currentX + i, currentY + j))
                    elif self.team == "Black" and board[currentY + j][currentX + i].team == "White":
                        availableCaptures.append((currentX + i, currentY + j))

        for i in list2:
            for j in list1:
                if not Piece.outOfBounds(currentX + i, currentY + j) and board[currentY + j][currentX + i]:
                    if self.team == "White" and board[currentY + j][currentX + i].team == "Black":
                        availableCaptures.append((currentX + i, currentY + j))
                    elif self.team == "Black" and board[currentY + j][currentX + i].team == "White":
                        availableCaptures.append((currentX + i, currentY + j))


        if mode == 0:
            if self.isPieceBlockingCheck(currentX, currentY, board) or UtilityFunctions.isInCheck(board, self.team):  # if the piece is not blocking check, it can move freely, otherwise must test its moves
                return self.filterBadMoves(availableCaptures, currentX, currentY, board)

        return availableCaptures