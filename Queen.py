from Piece import Piece
from Rook import Rook
from Bishop import Bishop

class Queen(Piece):

    def availableMoves(self, currentX, currentY, board, mode = 0):
        # mode argument determines if this function should account for moves the put the king in check
        # when run with mode = 0, it does account for this. This is used in the main loop when deciding where a piece can move
        # mode = 1 is for simply finding all of a pieces possible moves.

        tempRook = Rook(self.team)
        tempBishop = Bishop(self.team)

        availableMoves = tempRook.availableMoves(currentX, currentY, board) + tempBishop.availableMoves(currentX, currentY, board)

        return availableMoves


    def availableCaptures(self, currentX, currentY, board, mode = 0):
        # mode argument determines if this function should account for moves the put the king in check
        # when run with mode = 0, it does account for this. This is used in the main loop when deciding where a piece can move
        # mode = 1 is for simply finding all of a pieces possible moves.

        availableCaptures = []

        tempRook = Rook(self.team)
        tempBishop = Bishop(self.team)

        availableCaptures = tempRook.availableCaptures(currentX, currentY, board, mode) + tempBishop.availableCaptures(currentX, currentY, board, mode)

        return availableCaptures