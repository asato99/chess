import sys
sys.path.append('..')
import unittest
from app.models.virtual_board import VirtualBoard
from app.models.game_master import GameMaster
from resource.data.board import BoardData

class TestVirtualBoard(unittest.TestCase):
    def setUp(self):
        print('set up')

    def test_update_board(self):
        # arrange
        gm = GameMaster()
        before_board = BoardData.init_board
        after_board = BoardData.e4_board
        virtualBoard = VirtualBoard(before_board, 'white', gm)
        move = [{'rank':6, 'file':4},{'rank':4, 'file':4}]

        # action
        board = virtualBoard.update_board(move)

        # assert
        self.assertEqual(board, after_board)

    def test_two_players_update_board(self):
        # arrange
        gm = GameMaster()
        before_board = BoardData.init_board
        after_board = BoardData.e4e5_board
        virtualBoard = VirtualBoard(before_board, 'white', gm)
        first_move = [{'rank':6, 'file':4},{'rank':4, 'file':4}]
        second_move = [{'rank':1, 'file':4},{'rank':3, 'file':4}]

        # action
        first_board = virtualBoard.update_board(first_move)
        second_board = virtualBoard.update_board(second_move)

        # assert
        self.assertEqual(second_board, after_board)

if __name__ == "__main__":
    unittest.main()