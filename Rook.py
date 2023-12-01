from Piece import Piece
from UtilityFunctions import UtilityFunctions


class Rook(Piece):

    def availableMoves(self, currentX, currentY, board, mode = 0):
        #mode argument determines if this function should account for moves the put the king in check
        #when run with mode = 0, it does account for this. This is used in the main loop when deciding where a piece can move
        #mode = 1 is for simply finding all of a pieces possible moves.

        availableMoves = []

        for i in range(currentX + 1, 8): #going right
            if board[currentY][i] == None:
                availableMoves.append((i, currentY))
            else:
                break

        for i in range(currentX - 1, -1, -1):  #going left
            if board[currentY][i] == None:
                availableMoves.append((i, currentY))
            else:
                break

        for i in range(currentY - 1, -1, -1):  #going up
            if board[i][currentX] == None:
                availableMoves.append((currentX, i))
            else:
                break

        for i in range(currentY + 1, 8):  #going down
            if board[i][currentX] == None:
                availableMoves.append((currentX, i))
            else:
                break

        if mode == 0:
            if self.isPieceBlockingCheck(currentX, currentY, board) or UtilityFunctions.isInCheck(board, self.team):  # if the piece is not blocking check, it can move freely, otherwise must test its moves
                return self.filterBadMoves(availableMoves, currentX, currentY, board)

        return availableMoves


    def availableCaptures(self, currentX, currentY, board, mode = 0):
        # mode argument determines if this function should account for moves the put the king in check
        # when run with mode = 0, it does account for this. This is used in the main loop when deciding where a piece can move
        # mode = 1 is for simply finding all of a pieces possible moves.

        availableCaptures = []

        for i in range(currentX + 1, 8):  # going right
            if board[currentY][i]:
                if self.team == "White" and board[currentY][i].team == "Black":
                    availableCaptures.append((i, currentY))
                elif self.team == "Black" and board[currentY][i].team == "White":
                    availableCaptures.append((i, currentY))
                break


        for i in range(currentX - 1, -1, -1):  # going left
            if board[currentY][i]:
                if self.team == "White" and board[currentY][i].team == "Black":
                    availableCaptures.append((i, currentY))
                elif self.team == "Black" and board[currentY][i].team == "White":
                    availableCaptures.append((i, currentY))
                break


        for i in range(currentY - 1, -1, -1):  # going up
            if board[i][currentX]:
                if self.team == "White" and board[i][currentX].team == "Black":
                    availableCaptures.append((currentX, i))
                elif self.team == "Black" and board[i][currentX].team == "White":
                        availableCaptures.append((currentX, i))
                break


        for i in range(currentY + 1, 8):  # going down
            if board[i][currentX]:
                if self.team == "White" and board[i][currentX].team == "Black":
                    availableCaptures.append((currentX, i))
                elif self.team == "Black" and board[i][currentX].team == "White":
                    availableCaptures.append((currentX, i))
                break

        if mode == 0:
            if self.isPieceBlockingCheck(currentX, currentY, board) or UtilityFunctions.isInCheck(board, self.team): #if the piece is not blocking check and the king is not in check, it can move freely, otherwise must test its moves
                return self.filterBadMoves(availableCaptures, currentX, currentY, board)

        return availableCaptures