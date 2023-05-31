class GameMaster():

	def __init__(self):
		self.before = None
		self.availSC = {'white': True, 'black': True}
		self.availLC = {'white': True, 'black': True}

	def set_before(self, before):
		self.before = before

	def get_before(self):
		return self.before
	
	def set_avail_sc(self, side, value):
		self.availSC[side] = value

	def get_avail_sc(self, side):
		return self.availSC[side]

	def set_avail_lc(self, side, value):
		self.availLC[side] = value

	def get_avail_lc(self, side):
		return self.availLC[side]
