class Bowling(object):

	def __init__(self):
		self.score = [0]*10
		self.first_throw = True
		self.frame = 0
		self.strike_a_index = -1 #
		self.strike_b_index = -1
		self.spare_index = -1



	def throw(self, knocked):

		if not check_throw(knocked):
			break
		if not check_frame():
			break




		self.score[self.frame] += knocked

		if(first_throw):
			first_throw = False
			if knocked == 10:
				first_throw = True
				self.frame += 1
				#strike
		else:
			first_throw = True
			self.frame += 1
			if(self.score[self.frame] == 10):
				#frame	











		else:
			print ('Invalid throw, try again.')

		#if self.first_throw:
		#	self.score.append(knocked)
		#	self.first_throw = False


	def check_throw(self, knocked):
		if knocked >= 0 or knocked <=10:
			return True
		else:
			return False

	def check_frame(self):
		if self.score[self.frame] <= 10 or self.score[self.frame] >= 0:
			return True
		else:
			return False




