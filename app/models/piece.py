class Piece():
    def __init__(self, side):
        self.side = side

    def set_side(self, side):
        self.side = side


class Pawn(Piece):
    def __init__(self, side):
        self.side = side
        self.moves = []

    def possible_move(self, board, square, before):
        moves = []
        if self.side == 'white':
            if square['rank'] == 0:
                return moves
            
            # takes
            if square['file'] < 7 and get_ini_letter(board[square['rank']-1][square['file']+1]) == 'b':
                moveSquare = {'rank': square['rank']-1, 'file': square['file']+1}
                moves.append([square, moveSquare])
            if square['file'] > 0 and get_ini_letter(board[square['rank']-1][square['file']-1]) == 'b':
                moveSquare = {'rank': square['rank']-1, 'file': square['file']-1}
                moves.append([square, moveSquare])

            # advance
            if board[square['rank']-1][square['file']] == '':
                moveSquare = {'rank': square['rank']-1, 'file': square['file']}
                moves.append([square, moveSquare])

            # initial position
            if square['rank'] == 6 and board[5][square['file']] == '' and board[4][square['file']] == '':
                moveSquare = {'rank':4, 'file':square['file']}
                moves.append([square, moveSquare])

            # en passant
            if before is not None and square['rank'] == 3 and square['file'] < 7 and board[3][square['file']+1] == 'bp' and before[0]['rank'] == 1 and before[0]['file'] == square['file']+1 and before[1]['rank'] == 3 and before[1]['file'] == square['file']+1:
                moveSquare = {'rank':2, 'file':square['file']+1}
                moves.append([square, moveSquare])
            if before is not None and square['rank'] == 3 and square['file'] > 0 and board[3][square['file']-1] == 'bp' and before[0]['rank'] == 1 and before[0]['file'] == square['file']-1 and before[1]['rank'] == 3 and before[1]['file'] == square['file']-1:
                moveSquare = {'rank':2, 'file':square['file']-1}
                moves.append([square, moveSquare])

        else:
            if square['rank'] == 7:
                return moves

            # takes
            if square['file'] < 7 and get_ini_letter(board[square['rank']+1][square['file']-1]) == 'w':
                moveSquare = {'rank': square['rank']+1, 'file': square['file']+1}
                moves.append([square, moveSquare])
            if square['file'] > 0 and get_ini_letter(board[square['rank']+1][square['file']-1]) == 'w':
                moveSquare = {'rank': square['rank']+1, 'file': square['file']-1}
                moves.append([square, moveSquare])

            # advance
            if board[square['rank']+1][square['file']] == '':
                moveSquare = {'rank': square['rank']+1, 'file': square['file']}
                moves.append([square, moveSquare])

            # initial position
            if square['rank'] == 1 and board[2][square['file']] == '' and board[3][square['file']] == '':
                moveSquare = {'rank':3, 'file':square['file']}
                moves.append([square, moveSquare])

            # en passant
            if before is not None and square['rank'] == 4 and square['file'] < 7 and board[4][square['file']+1] == 'bp' and before[0]['rank'] == 6 and before[0]['file'] == square['file']+1 and before[1]['rank'] == 4 and before[1]['file'] == square['file']+1:
                moveSquare = {'rank':5, 'file':square['file']+1}
                moves.append([square, moveSquare])
            if before is not None and square['rank'] == 4 and square['file'] > 0 and board[4][square['file']-1] == 'bp' and before[0]['rank'] == 6 and before[0]['file'] == square['file']-1 and before[1]['rank'] == 4 and before[1]['file'] == square['file']-1:
                moveSquare = {'rank':5, 'file':square['file']-1}
                moves.append([square, moveSquare])


        return moves 
            
    def get_dominant_squares(self, board, square, side):
        moves = []

        if side == 'white':
            if square['rank'] > 0:
                moves.append([square, {'rank': square['rank']-1, 'file': square['file']+1}])
                moves.append([square, {'rank': square['rank']-1, 'file': square['file']-1}])

        else:
            if square['rank'] < 7:
                moves.append([square, {'rank': square['rank']+1, 'file': square['file']+1}])
                moves.append([square, {'rank': square['rank']+1, 'file': square['file']-1}])

        return moves 

class Rook(Piece):
    def __init__(self, side):
        self.side = side
        self.moves = []

    def possible_move(self, board, square):
        moves = self.get_dominant_squares(board, square, self.side)
        return moves

    def get_dominant_squares(self, board, square, side):
        moves = []
        directions = ['n', 's', 'e', 'w']

        for d in directions:
            linerMoves = get_liner_moves(side, board, square, d)
            moves.extend(linerMoves)

        return moves


class Knight(Piece):
    def __init__(self, side):
        self.side = side
        self.moves = []

    def possible_move(self, board, square):
        moves = self.get_dominant_squares(board,square, self.side)
        return moves

    def get_dominant_squares(self, board, square, side):
        moves = []

        for l in [2, -2]:
            for s in [1, -1]:
                moveSquare = {'rank': square['rank']+l, 'file': square['file']+s}
                if check_in_boundary(moveSquare) and not check_on_buddy(board, moveSquare, side):
                    moves.append([square, moveSquare])

                moveSquare = {'rank': square['rank']+s, 'file': square['file']+l}
                if check_in_boundary(moveSquare) and not check_on_buddy(board, moveSquare, side):
                    moves.append([square, moveSquare])

        return moves


class Bishop(Piece):
    def __init__(self, side):
        self.side = side
        self.moves = []

    def possible_move(self, board, square):
        moves = self.get_dominant_squares(board, square, self.side)
        return moves

    def get_dominant_squares(self, board, square, side):
        moves = []
        directions = ['ne', 'se', 'sw', 'nw']

        for d in directions:
            diagonalMoves = get_diagonal_moves(side, board, square, d)
            moves.extend(diagonalMoves)

        return moves


class Queen(Piece):
    def __init__(self, side):
        self.side = side
        self.moves = []

    def possible_move(self, board, square):
        moves = self.get_dominant_squares(board, square, self.side)
        return moves

    def get_dominant_squares(self, board, square, side):
        moves = []
        linerDirections = ['n', 's', 'e', 'w']
        diagonalDirections = ['ne', 'se', 'sw', 'nw']

        for d in linerDirections:
            linerMoves = get_liner_moves(side, board, square, d)
            moves.extend(linerMoves)

        for d in diagonalDirections:
            diagonalMoves = get_diagonal_moves(side, board, square, d)
            moves.extend(diagonalMoves)

        return moves

class King(Piece):
    def __init__(self, side):
        self.side = side
        self.moves = []

    def possible_move(self, board, square, oppodominant, availsc, availlc):
        moves = self.get_dominant_squares(board, square, self.side)
        return moves

        # for castling
        if self.side == 'white':
            sctrace = [
                {'rank': 7, 'file': 4},
                {'rank': 7, 'file': 5},
                {'rank': 7, 'file': 6},
            ]
            lctrace = [
                {'rank': 7, 'file': 4},
                {'rank': 7, 'file': 3},
                {'rank': 7, 'file': 2},
                {'rank': 7, 'file': 1},
            ]
        else:
            sctrace = [
                {'rank': 0, 'file': 4},
                {'rank': 0, 'file': 5},
                {'rank': 0, 'file': 6},
            ]
            lcTrace = [
                {'rank': 0, 'file': 4},
                {'rank': 0, 'file': 3},
                {'rank': 0, 'file': 2},
                {'rank': 0, 'file': 1},
            ]
                    
        checkTrace = True
        if availSC:
            for mv in oppoDominant:
                for index, t in enumerate(scTrace):
                    if mv[0]['rank'] == t['rank'] and mv[0]['file'] == t['file']:
                        checkTrace = False
                    if index != 0 and board[t['rank']][t['file']] != '':
                        checkTrace = False
        if checkTrace:
            moves.append([square, scTrace[2]])

        checkTrace = True
        if availLC:
            for mv in oppoDominant:
                for index, t in enumerate(lcTrace):
                    if  index != 3 and mv[0]['rank'] == t['rank'] and mv[0]['file'] == t['file']:
                        checkTrace = False
                    if index != 0 and board[t['rank']][t['file']] != '':
                        checkTrace = False
        if checkTrace:
            moves.append([square, lcTrace[2]])

        return moves

    def get_dominant_squares(self, board, square, side):
        moves = []

        for r in [0, 1, -1]:
            for f in [0, 1, -1]:
                if r == 0 and f == 0:
                    continue

                moveSquare = {'rank': square['rank']+r, 'file': square['file']+f}
                if check_in_boundary(moveSquare) and not check_on_buddy(board, moveSquare, side):
                    moves.append([square, moveSquare])

        return moves

class AmbigPiece():
    def __init__(self, side):
        self.side = side
        self.pawn = Pawn(side)
        self.rook = Rook(side)
        self.knight = Knight(side)
        self.bishop = Bishop(side)
        self.queen = Queen(side)
        self.king = King(side)

    def set_side(self, side):
        self.side = side
        self.pawn.set_side(side)
        self.rook.set_side(side)
        self.knight.set_side(side)
        self.bishop.set_side(side)
        self.queen.set_side(side)
        self.king.set_side(side)

    def get_dominant_squares(self, board, square, side):
        dominantSquares = []

        initial = side[0]
        piece = board[square['rank']][square['file']]

        if piece == initial + 'p':
            squares = self.pawn.get_dominant_squares(board, square, side)
            dominantSquares.extend(squares)

        elif piece == initial + 'r':
            squares = self.rook.get_dominant_squares(board, square, side)
            dominantSquares.extend(squares)

        elif piece == initial + 'n':
            squares = self.knight.get_dominant_squares(board, square, side)
            dominantSquares.extend(squares)

        elif piece == initial + 'b':
            squares = self.bishop.get_dominant_squares(board, square, side)
            dominantSquares.extend(squares)

        elif piece == initial + 'q':
            squares = self.queen.get_dominant_squares(board, square, side)
            dominantSquares.extend(squares)

        elif piece == initial + 'k':
            squares = self.king.get_dominant_squares(board, square, side)
            dominantSquares.extend(squares)

        return dominantSquares

    def possible_move(self, board, square, before, oppoDominant, availSC, availLC):
        possibleMoves = []

        initial = self.side[0]
        piece = board[square['rank']][square['file']]

        if piece == initial + 'p':
            moves = self.pawn.possible_move(board, square, before)
            possibleMoves.extend(moves)

        if piece == initial + 'r':
            moves = self.rook.possible_move(board, square)
            possibleMoves.extend(moves)

        if piece == initial + 'n':
            moves = self.knight.possible_move(board, square)
            possibleMoves.extend(moves)

        if piece == initial + 'b':
            moves = self.bishop.possible_move(board, square)
            possibleMoves.extend(moves)

        if piece == initial + 'q':
            moves = self.queen.possible_move(board, square)
            possibleMoves.extend(moves)

        if piece == initial + 'k':
            moves = self.king.possible_move(board, square, oppoDominant, availSC, availLC)
            possibleMoves.extend(moves)

        return possibleMoves


### funcitons
def check_in_boundary(square):
    if square['rank'] >= 0 and square['rank'] <= 7 and square['file'] >= 0 and square['file'] <= 7:
        return True
    else:
        return False

def get_ini_letter(word):
    if len(word) > 0:
        return word[0]
    else:
        return ''

def check_on_buddy(board, square, side):
    if get_ini_letter(board[square['rank']][square['file']]) == get_ini_letter(side):
        return True
    else:
        False


def get_opposite_side(side):
    if side == 'white':
        return 'black'
    else:
        return 'white'

def get_liner_moves(side, board, square, direction):        
    moves = []
    moveSquare = square

    while True:
        if direction == 'n':
            moveSquare = {'rank': moveSquare['rank']-1, 'file': moveSquare['file']}
        elif direction == 's':
            moveSquare = {'rank': moveSquare['rank']+1, 'file': moveSquare['file']}
        elif direction == 'e':
            moveSquare = {'rank': moveSquare['rank'], 'file': moveSquare['file']+1}
        else:
            moveSquare = {'rank': moveSquare['rank'], 'file': moveSquare['file']-1}

        if not check_in_boundary(moveSquare):
            break

        piece = board[moveSquare['rank']][moveSquare['file']]
        if piece != '':
            if get_ini_letter(piece) != get_ini_letter(side):
                moves.append([square,  moveSquare])
            break
        else:
            moves.append([square,  moveSquare])

    return moves

def get_diagonal_moves(side, board, square, direction):        
    moves = []
    moveSquare = square

    while True:
        if direction == 'ne':
            moveSquare = {'rank': moveSquare['rank']-1, 'file': moveSquare['file']+1}
        elif direction == 'se':
            moveSquare = {'rank': moveSquare['rank']+1, 'file': moveSquare['file']+1}
        elif direction == 'sw':
            moveSquare = {'rank': moveSquare['rank']+1, 'file': moveSquare['file']-1}
        else:
            moveSquare = {'rank': moveSquare['rank']-1, 'file': moveSquare['file']-1}

        if not check_in_boundary(moveSquare):
            break

        piece = board[moveSquare['rank']][moveSquare['file']]
        if piece != '':
            if get_ini_letter(piece) != get_ini_letter(side):
                moves.append([square,  moveSquare])
            break
        else:
            moves.append([square,  moveSquare])

    return moves