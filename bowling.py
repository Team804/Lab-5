class Bowling(object):
	score = []
	first_throw = True
	frame = 0
	strike_a_index = -1  #
	strike_b_index = -1
	spare_index = -1

	def __init__(self):
		self.score = [0] *10
		self.first_throw = True
		self.frame = 0


	def throw(self, knocked):
		# bad throw
		if self.check_bad_throw(knocked):
			return -1;

		self.score[self.frame] = knocked

        if first_throw == False:
            firstFrame = False
        else:
            firstFrame = True
            frame += 1


	def check_bad_throw (self, knocked):
		if knocked < 0 or knocked > 10:
			return True
		return False

	def check_frame(self):
		if self.score[self.frame] <= 10 or self.score[self.frame] >= 0:
			return True
		else:
			return False
