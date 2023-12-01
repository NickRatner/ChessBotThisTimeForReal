from Piece import Piece
from UtilityFunctions import UtilityFunctions
import copy

class King(Piece):

    def availableMoves(self, currentX, currentY, board, mode = 0):
        # mode argument determines if this function should account for moves the put the king in check
        # when run with mode = 0, it does account for this. This is used in the main loop when deciding where a piece can move
        # mode = 1 is for simply finding all of a pieces possible moves.

        availableMoves = []

        for i in range(-1, 2):
            for j in range(-1, 2):
                if not Piece.outOfBounds(currentX + i, currentY + j) and board[currentY + j][currentX + i] == None:
                    availableMoves.append((currentX + i, currentY + j))


        if self.team == "White":
            #castling left
            if not self.hasMoved and board[7][0] and not board[7][0].hasMoved: #if the king, and the left rook both havn't moved
                if board[7][1] == None and board[7][2] == None and board[7][3] == None and not UtilityFunctions.isInCheck(board, self.team): #if the 3 squares between them are not empty
                    # check the squares in between are not checked
                    tempBoard = copy.deepcopy(board)
                    tempBoard[7][2] = King(self.team)
                    tempBoard[7][4] = None
                    if not UtilityFunctions.isInCheck(tempBoard, self.team):

                        tempBoard = copy.deepcopy(board)
                        tempBoard[7][3] = King(self.team)
                        tempBoard[7][4] = None
                        if not UtilityFunctions.isInCheck(tempBoard, self.team):

                            availableMoves.append((2,7))

                    #move rook (will do this in main.py if castling occurs)

            #castling right
            if not self.hasMoved and board[7][7] and not board[7][7].hasMoved: #if the king, and the left rook both havn't moved
                if board[7][6] == None and board[7][5] == None and not UtilityFunctions.isInCheck(board, self.team): #if the 3 squares between them are not empty
                    # check the squares in between are not checked
                    tempBoard = copy.deepcopy(board)
                    tempBoard[7][5] = King(self.team)
                    tempBoard[7][4] = None
                    if not UtilityFunctions.isInCheck(tempBoard, self.team):

                        tempBoard = copy.deepcopy(board)
                        tempBoard[7][6] = King(self.team)
                        tempBoard[7][4] = None
                        if not UtilityFunctions.isInCheck(tempBoard, self.team):

                            availableMoves.append((6,7))

                    #move rook

        elif self.team == "Black":
            # castling left
            if not self.hasMoved and board[0][0] and not board[0][0].hasMoved:  # if the king, and the left rook both havn't moved
                if board[0][1] == None and board[0][2] == None and board[0][3] == None and not UtilityFunctions.isInCheck(board,
                                                                  self.team):  # if the 3 squares between them are not empty
                    # check the squares in between are not checked
                    tempBoard = copy.deepcopy(board)
                    tempBoard[0][2] = King(self.team)
                    tempBoard[0][4] = None
                    if not UtilityFunctions.isInCheck(tempBoard, self.team):

                        tempBoard = copy.deepcopy(board)
                        tempBoard[0][3] = King(self.team)
                        tempBoard[0][4] = None
                        if not UtilityFunctions.isInCheck(tempBoard, self.team):
                            availableMoves.append((2, 0))

                    # move rook (will do this in main.py if castling occurs)

            # castling right
            if not self.hasMoved and board[0][7] and not board[0][7].hasMoved:  # if the king, and the left rook both havn't moved
                if board[0][6] == None and board[0][5] == None and not UtilityFunctions.isInCheck(board,
                                                                                                  self.team):  # if the 3 squares between them are not empty
                    # check the squares in between are not checked
                    tempBoard = copy.deepcopy(board)
                    tempBoard[0][5] = King(self.team)
                    tempBoard[0][4] = None
                    if not UtilityFunctions.isInCheck(tempBoard, self.team):

                        tempBoard = copy.deepcopy(board)
                        tempBoard[0][6] = King(self.team)
                        tempBoard[0][4] = None
                        if not UtilityFunctions.isInCheck(tempBoard, self.team):
                            availableMoves.append((6, 0))

                    # move rook



        if mode == 0:
            return self.filterBadMoves(availableMoves, currentX, currentY, board)

        return availableMoves


    def availableCaptures(self, currentX, currentY, board, mode = 0):
        # mode argument determines if this function should account for moves the put the king in check
        # when run with mode = 0, it does account for this. This is used in the main loop when deciding where a piece can move
        # mode = 1 is for simply finding all of a pieces possible moves.

        availableCaptures = []

        for i in range(-1, 2):
            for j in range(-1, 2):
                if not Piece.outOfBounds(currentX + i, currentY + j) and board[currentY + j][currentX + i]:
                    if self.team == "White" and board[currentY + j][currentX + i].team == "Black":
                        availableCaptures.append((currentX + i, currentY + j))

                    elif self.team == "Black" and board[currentY + j][currentX + i].team == "White":
                        availableCaptures.append((currentX + i, currentY + j))

        if mode == 0:
            return self.filterBadMoves(availableCaptures, currentX, currentY, board)

        return availableCaptures