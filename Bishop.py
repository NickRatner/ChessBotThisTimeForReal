from Piece import Piece
from UtilityFunctions import UtilityFunctions

class Bishop(Piece):

    def availableMoves(self, currentX, currentY, board, mode = 0):
        # mode argument determines if this function should account for moves the put the king in check
        # when run with mode = 0, it does account for this. This is used in the main loop when deciding where a piece can move
        # mode = 1 is for simply finding all of a pieces possible moves.

        availableMoves = []

        x = currentX + 1  # tracking the horizontal position
        y = currentY - 1  # tracking the vertical position
        while not Piece.outOfBounds(x, y):  # going up and right
            if board[y][x] == None:
                availableMoves.append((x, y))
            else:
                break
            x += 1
            y -= 1

        x = currentX - 1
        y = currentY - 1
        while not Piece.outOfBounds(x, y):  # going up and left
            if board[y][x] == None:
                availableMoves.append((x, y))
            else:
                break
            x -= 1
            y -= 1

        x = currentX + 1
        y = currentY + 1
        while not Piece.outOfBounds(x, y):  # going down and right
            if board[y][x] == None:
                availableMoves.append((x, y))
            else:
                break
            x += 1
            y += 1

        x = currentX - 1
        y = currentY + 1
        while not Piece.outOfBounds(x, y):  # going down and left
            if board[y][x] == None:
                availableMoves.append((x, y))
            else:
                break
            x -= 1
            y += 1

        if mode == 0:
            if self.isPieceBlockingCheck(currentX, currentY, board) or UtilityFunctions.isInCheck(board, self.team):  # if the piece is not blocking check, it can move freely, otherwise must test its moves
                return self.filterBadMoves(availableMoves, currentX, currentY, board)

        return availableMoves


    def availableCaptures(self, currentX, currentY, board, mode = 0):
        # mode argument determines if this function should account for moves the put the king in check
        # when run with mode = 0, it does account for this. This is used in the main loop when deciding where a piece can move
        # mode = 1 is for simply finding all of a pieces possible moves.

        availableCaptures = []

        x = currentX + 1  # tracking the horizontal position
        y = currentY - 1  # tracking the vertical position
        while not Piece.outOfBounds(x, y):  # going up and right
            if board[y][x]:
                if self.team == "White" and board[y][x].team == "Black":
                    availableCaptures.append((x, y))
                elif self.team == "Black" and board[y][x].team == "White":
                    availableCaptures.append((x, y))
                break
            x += 1
            y -= 1

        x = currentX - 1
        y = currentY - 1
        while not Piece.outOfBounds(x, y):  # going up and left
            if board[y][x]:
                if self.team == "White" and board[y][x].team == "Black":
                    availableCaptures.append((x, y))
                elif self.team == "Black" and board[y][x].team == "White":
                    availableCaptures.append((x, y))
                break

            x -= 1
            y -= 1

        x = currentX + 1
        y = currentY + 1
        while not Piece.outOfBounds(x, y):  # going down and right
            if board[y][x]:
                if self.team == "White" and board[y][x].team == "Black":
                    availableCaptures.append((x, y))
                elif self.team == "Black" and board[y][x].team == "White":
                    availableCaptures.append((x, y))
                break

            x += 1
            y += 1

        x = currentX - 1
        y = currentY + 1
        while not Piece.outOfBounds(x, y):  # going down and left
            if board[y][x]:
                if self.team == "White" and board[y][x].team == "Black":
                    availableCaptures.append((x, y))
                elif self.team == "Black" and board[y][x].team == "White":
                    availableCaptures.append((x, y))
                break

            x -= 1
            y += 1


        if mode == 0:
            if self.isPieceBlockingCheck(currentX, currentY, board) or UtilityFunctions.isInCheck(board, self.team):  # if the piece is not blocking check, it can move freely, otherwise must test its moves
                return self.filterBadMoves(availableCaptures, currentX, currentY, board)

        return availableCaptures