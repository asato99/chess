import sys
sys.path.append('..')
import unittest
from app.models.memory import Memory

class TestMemory(unittest.TestCase):
	def setUp(self):
		print('set up')
		self.memory = Memory()

	def test_first_add_select_move(self):
		# arrange
		move = [{'rank':1, 'file':1}, {'rank':2, 'file':1}]

		# act
		self.memory.add_select_move(move)

		# assert
		expected = {'move': move, 'opponent':[]}
		actual = moveMemory = self.memory.get_move_memory()
		self.assertEqual(expected, actual)

	def test_first_add_opponent_moves(self):
		# arrange
		move = [{'rank':1, 'file':1}, {'rank':2, 'file':1}]
		self.memory.add_select_move(move)
		opponentMoves = [
			[{'rank':6, 'file':1}, {'rank':5, 'file':1}],
			[{'rank':6, 'file':2}, {'rank':5, 'file':2}],
			[{'rank':6, 'file':3}, {'rank':5, 'file':3}],
		]

		# act
		self.memory.add_opponent_moves(opponentMoves)

		# assert
		opponent = [
			{'move': [{'rank':6, 'file':1}, {'rank':5, 'file':1}], 'memory': {'move': None, 'opponent':[]}},
			{'move': [{'rank':6, 'file':2}, {'rank':5, 'file':2}], 'memory': {'move': None, 'opponent':[]}},
			{'move': [{'rank':6, 'file':3}, {'rank':5, 'file':3}], 'memory': {'move': None, 'opponent':[]}},
		]
		expected = {'move': move, 'opponent':opponent}
		actual = moveMemory = self.memory.get_move_memory()
		self.assertEqual(expected, actual)

if __name__ == '__main__':
	unittest.main()