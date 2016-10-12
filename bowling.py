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
        self.score = [0] * 10
        self.spareArray = [False] * 10
        self.strikeArray = [False] * 10
        self.first_throw = True
        self.frame = 0


    def throw(self, knocked):
        # bad throw
        if self.check_bad_throw(knocked):
            return -1
        # if check frame score fails at end of frame
        if self.check_frame == False:
               # throw exception?
            return -1
        if self.frame >= 10:
            return -1

        self.score[self.frame] += knocked
                
        if self.first_throw == True:
            if knocked == 10:
                self.strikeArray[self.frame] = True
                self.check_strike_spare_scoring
                self.frame += 1
            self.first_throw = False
        else:
            if knocked == 10:
                self.spareArray[self.frame] = True
            self.check_strike_spare_scoring
            self.first_throw = True
            self.frame += 1
            self.firstFrame = False



    def check_bad_throw (self, knocked):
        if knocked < 0 or knocked > 10:
            return True
        return False

    def check_frame(self):
        if self.score[self.frame] <= 10 or self.score[self.frame] >= 0:
            return True
        else:
            return False

    def check_strike_spare_scoring(self):
         #strike and spare scoring
        if self.frame >= 1:
            if self.spareArray[self.frame - 1] == True:
                self.score[self. frame - 1] += self.score[self.frame]
        if self.frame >= 2:
            if self.strikeArray[self.frame - 2] == True:
                self.score[self.frame - 2] += self.score[self.frame - 1] + self.score[self.frame]
