import copy

class Memory():
	def __init__(self):
		self.history = []
		self.historyBk = []
		self.moveMemory = {'move': None, 'opponent': []}

	def add_select_move(self, move):
		memory = self.__get_target_memory()
		memory['move'] = move

		# if len(self.history) == 0:
		# 	self.moveMemory = { 'move': move, 'opponent': []}
		# 	return

		# memory = self.moveMemory
		# while len(self.history) > 0:
		# 	hMove = self.history.pop(0)
		# 	self.historyBk.append(hMove)
		# 	opponent = memory['opponent']
		# 	for op in opponent:
		# 		if self.__match_move(op['move'],hMove):
		# 			if len(self.history) == 0:
		# 				op['memory'] = {'move': move, 'opponent': []}
		# 				break
		# 			else:
		# 				memory = op['memory']
					

	def add_opponent_moves(self, moves):
		opponent = []
		for move in moves:
			opponent.append({'move':move, 'memory':{'move': None, 'opponent':[]}})
			
		memory = self.__get_target_memory()
		memory['opponent'] = opponent

	def add_history(self, move):
		self.history.append(move)

	def remove_history(self):
		self.history.pop()

	def get_move_memory(self):
		return self.moveMemory

	def __get_target_memory(self):
		memory = self.moveMemory
		while len(self.history) > 0:
			hMove = self.history.pop(0)
			self.historyBk.append(hMove)
			opponent = memory['opponent']
			for op in opponent:
				if self.__match_move(op['move'],hMove):
					memory = op['memory']
					if len(self.history) == 0:
						break

		self.history = copy.deepcopy(self.historyBk)

		return memory

		
	def __match_move(self, move1, move2):
		if (move1[0]['rank'] == move2[0]['rank'] and move1[0]['file'] and move2[0]['file']
			and move1[1]['rank'] == move2[1]['rank'] and move1[1]['file'] and move2[1]['file']):
			return True
		else:
			return False