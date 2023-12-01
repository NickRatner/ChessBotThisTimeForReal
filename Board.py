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