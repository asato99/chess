class Memory():
	def __init__(self):
		self.history = []
		self.historyBk = []
		self.moveMemory = { 'move': None, 'opponent': []}

	def add_move(self, move):
		hMove = self.history.pop(0)
		opponent = self.moveMemory['opponent']
		for op in opponent:
			if self.__match_move(op['move'],hMove):
				if len(self.history) == 0:
					op['memory'] = { 'move': move, 'opponent': []}
				else:
					memory = op['memory']
					
		
	def __match_move(self, move1, move2):
		if move1[0]['rank'] == move2[0]['rank'] and move1[0]['file'] and move2[0]['file']
			and move1[1]['rank'] == move2[1]['rank'] and move1[1]['file'] and move2[1]['file']:
			return True
		else:
			return False