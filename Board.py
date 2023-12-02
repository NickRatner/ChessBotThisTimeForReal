from Bishop import Bishop
from King import King
from Knight import Knight
from Pawn import Pawn
from Queen import Queen
from Rook import Rook


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
        self.board[oldY][oldX] = None

        # Pawn promotion
        if str(type(self.board[newY][newX])) == "<class 'Pawn.Pawn'>":
            if newY == 0 and self.board[newY][newX].team == "White":
                self.board[newY][newX] = Queen("White")

            elif newY == 7 and self.board[newY][newX].team == "Black":
                self.board[newY][newX] = Queen("Black")