from .piece import AmbigPiece
import copy

class VirtualBoard():

    def __init__(self, board, side, gm):

        self.ambPiece = AmbigPiece(side)

        self.board = copy.deepcopy(board)
        self.side = copy.deepcopy(side)
        self.before = copy.deepcopy(gm.get_before())
        self.availSC = copy.deepcopy(gm.get_avail_sc(side))
        self.availLC = copy.deepcopy(gm.get_avail_lc(side))

        # self.initBoard = board
        # self.initSide = side
        # self.initBefore = gm.get_before()
        # self.initAvailSC = gm.get_avail_sc(side)
        # self.initAvailLC = gm.get_avail_lc(side)

    # def sync_init(self):
    #     self.board = copy.deepcopy(self.initBoard)
    #     self.side = copy.deepcopy(self.initSide)
    #     self.before = copy.deepcopy(self.initBefore)
    #     self.availSC = copy.deepcopy(self.initAvailSC)
    #     self.availLC = copy.deepcopy(self.initAvailLC)

    def get_opposite_side(self):
        if self.side == 'white':
            return 'black'
        else:
            return 'white'

    def __get_king_square(self):
        kingSquare = {'rank': 0, 'file': 0}
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == self.side[0]+'k':
                    kingSquare = {'rank': i, 'file': j}
                    break

        return kingSquare

    def __is_checked(self):
        kingSquare = self.__get_king_square()
        oppoDominant = self.__get_dominant_squares(self.get_opposite_side())
        isChecked = False
        for squares in oppoDominant:
            if squares[1]['rank'] == kingSquare['rank'] and squares[1]['file'] == kingSquare['file']:
                isChecked = True
                break
        return isChecked

    def __get_checked_list(self):
        checkedList = []
        kingSquare = self.__get_king_square()
        oppoDominantSquares = self.__get_dominant_squares(self.get_opposite_side())
        for squares in oppoDominantSquares:
            if squares[1]['rank'] == kingSquare['rank'] and squares[1]['file'] == kingSquare['file']:
                checkedList.append(squares)

        return checkedList

    def get_board(self):
        board = copy.deepcopy(self.board)
        return board

    def set_board(self, board):
        self.board = copy.deepcopy(board)

    def set_side(self, side):
        self.side = copy.deepcopy(side)
        self.ambPiece.set_side(side)

    def change_side(self):
        self.side = self.get_opposite_side()

    def __get_dominant_squares(self, side):
        dominantSquares = []
        for i in range(8):
            for j in range(8):
                square = {'rank':i, 'file':j}
                squares = self.ambPiece.get_dominant_squares(self.board, square, side)
                dominantSquares.extend(squares)

        return dominantSquares

    def get_legal_moves(self):
        legalMoves = []

        possibleMoves = []
        oppoDominantSquares = self.__get_dominant_squares(self.get_opposite_side())
        for i in range(8):
            for j in range(8):
                square = {'rank':i, 'file':j}
                moves = self.ambPiece.possible_move(self.board, square, self.before, oppoDominantSquares, self.availSC, self.availLC)
                possibleMoves.extend(moves)

        board = self.get_board()
        for move in possibleMoves:
            self.set_board(board)
            self.update_board(move)
            if not self.__is_checked():
                legalMoves.append(move)

        return legalMoves

    def update_board(self, move):
        piece = self.board[move[0]['rank']][move[0]['file']]
        
        self.board[move[0]['rank']][move[0]['file']] = ''
        self.board[move[1]['rank']][move[1]['file']] = piece
        board = copy.deepcopy(self.board)

        return board
        

    def is_mated(self):
        legalMoves = self.get_legal_moves()
        if len(legalMoves) == 0 and self.__is_checked():
            return True
        else:
            return False

    def is_stale_mated(self):
        legalMoves = self.get_legal_moves()
        if len(legalMoves) == 0 and  not self.__is_checked():
            return True
        else:
            return False

def get_ini_letter(word):
    if len(word) > 0:
        return word[0]
    else:
        return ''
    
    