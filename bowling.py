class Bowling(object):
	score = []
        spareArray = []
        strikeArray = []
	first_throw = True
	frame = 0
	strike_a_index = -1  #
	strike_b_index = -1
	spare_index = -1

	def __init__(self):
		self.score = [0] *10
                self.spareArray = [0] * 10
                self.strikeArray = [0] * 10
		self.first_throw = True
		self.frame = 0


	def throw(self, knocked):
		# bad throw
		if self.check_bad_throw(knocked):
			return -1;

		self.score[self.frame] += knocked
                #if check frame score fails at end of frame
                if check_frame == False:
                       #throw exception?
                
        if first_throw == False:
            if knocked == 10:
                strikeArray[frame] = True
            firstFrame = False
        else:
            if knocked == 10:
                spareArray[frame] = True
            #strike and spare scoring
            if frame > 1:
                 if strikeArray[frame - 1] == True:
                     self.score[frame - 1] += knocked
                 if spareArray[frame - 1] == True:
                     self.score[frame - 1] += knocked
            if frame > 2:
                if strikeArray[frame - 2] == True:
                     self.score[frame - 2] += knocked
            
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
