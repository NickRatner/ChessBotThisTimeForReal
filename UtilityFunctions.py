
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