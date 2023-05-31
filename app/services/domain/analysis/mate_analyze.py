from models.virtual_board import VirtualBoard
from models.game_master import GameMaster
import copy

def search_one_move_mate(virtualBoard, board, side, gm):
	virtualBoard.set_board(board)
	virtualBoard.set_side(side)
	oppoSide = virtualBoard.get_opposite_side()
	legalMoves = virtualBoard.get_legal_moves()
	matingMoves = []
	for move in legalMoves:
		updBoard = virtualBoard.update_board(move)
		virtualBoard.set_board(updBoard)
		virtualBoard.set_side(oppoSide)
		if virtualBoard.is_mated():
			matingMoves.append(move)

		virtualBoard.set_board(board)
		virtualBoard.set_side(side)

	return matingMoves

def mate_exist_check(virtualBoard, board, side, gm, depth):
	depth += 1
	virtualBoard.set_board(board)
	virtualBoard.set_side(side)
	oppoSide = virtualBoard.get_opposite_side()
	legalMoves = virtualBoard.get_legal_moves()
	for move in legalMoves:
		updBoard = virtualBoard.update_board(move)
		virtualBoard.set_board(updBoard)
		virtualBoard.set_side(oppoSide)
		if virtualBoard.is_mated():
			return True
		elif depth > 2:
			return False

		matedCheck = True
		opponentMoves = virtualBoard.get_legal_moves()
		for oppoMove in opponentMoves:
			upddBoard = virtualBoard.update_board(oppoMove)
			virtualBoard.set_board(upddBoard)
			virtualBoard.set_side(side)
			copyBoard = copy.deepcopy(upddBoard)
			if not search_mate(virtualBoard, copyBoard, side, gm, depth):
				matedCheck = False
				break

			virtualBoard.set_board(updBoard)
			virtualBoard.set_side(oppoSide)

		if matedCheck:
			return True

		virtualBoard.set_board(board)
		virtualBoard.set_side(side)

	return False

def search_mate(virtualBoard, board, side, gm, depth):
	depth += 1
	virtualBoard.set_board(board)
	virtualBoard.set_side(side)
	oppoSide = virtualBoard.get_opposite_side()
	legalMoves = virtualBoard.get_legal_moves()
	for move in legalMoves:
		updBoard = virtualBoard.update_board(move)
		virtualBoard.set_board(updBoard)
		virtualBoard.set_side(oppoSide)
		if virtualBoard.is_mated():
			return True
		elif depth > 2:
			return False

		matedCheck = True
		opponentMoves = virtualBoard.get_legal_moves()
		for oppoMove in opponentMoves:
			upddBoard = virtualBoard.update_board(oppoMove)
			virtualBoard.set_board(upddBoard)
			virtualBoard.set_side(side)
			copyBoard = copy.deepcopy(upddBoard)
			if not search_mate(virtualBoard, copyBoard, side, gm, depth):
				matedCheck = False
				break

			virtualBoard.set_board(updBoard)
			virtualBoard.set_side(oppoSide)

		if matedCheck:
			return True

		virtualBoard.set_board(board)
		virtualBoard.set_side(side)

	return False