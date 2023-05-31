from models.virtual_board import VirtualBoard
from models.piece import AmbigPiece

class Board():

    def __init__(self):
        self.board = [
            ['br', 'bn', 'bb', 'bq', 'bk', 'bb', 'bn', 'br'],
            ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
            ['wr', 'wn', 'wb', 'wq', 'wk', 'wb', 'wn', 'wr'],
        ]
        self.before = None
        self.side = 'white'
        self.ambPiece = AmbigPiece('white')
        self.availSC = True
        self.availLC = True

    def get_board(self):
        return self.board

    def set_board(self, board):
        self.board = board

    def set_side(self, side):
        self.side = side
        self.ambPiece.set_side(side)

def get_opposite_side(side):
    if side == 'white':
        return 'black'
    else:
        return 'white'
    
    