import unittest
from bowling import Bowling

class BowlingTest(unittest.TestCase):
	def setUp(self):
		self.bowling = Bowling()

	def tear(self):
		del self.bowling
		
	def test_one_throw(self):
		self.bowling.throw(3)
		self.assertEqual(self.bowling.score[0], 3)
		self.assertFalse(self.bowling.first_throw)
		self.assertEqual(self.bowling.frame, 0)

	def test_two_throws(self):
		self.bowling.throw(6)
		self.bowling.throw(2)
		self.assertEqual(self.bowling.score[0], 8)
		self.assertFalse(self.bowling.first_throw)
		self.assertEqual(self.bowling.frame, 1)

	def test_three_throws(self):
		self.bowling.throw(5)
		self.bowling.throw(4)
		self.assertEqual(self.bowling.score[0], 9)
		self.assertFalse(self.bowling.first_throw)
		self.assertEqual(self.bowling.frame, 1)
		self.bowling.throw(8)
		self.assertEqual(self.bowling.score[1], 8)
		self.assertEqual(self.bowling.frame, 1)

	def test_spare_counts_next_frame_score(self):
		self.bowling.throw(5)
		self.bowling.throw(5)
		self.assertEqual(self.bowling.frame, 1)
		self.bowling.throw(7)
		self.assertEqual(self.bowling.score[0], 17)
		self.assertEqual(self.bowling.score[1], 7)

	def test_strike_moves_to_next_frame(self):
		self.bowling.throw(10)
		self.assertEqual(self.bowling.frame, 1)
		self.bowling.throw(10)
		self.assertEqual(self.bowling.frame, 2)
		self.bowling.throw(5)
		self.assertEqual(self.bowling.frame, 2)
		self.bowling.throw(3)
		self.assertEqual(self.bowling.frame, 3)


	def test_strike_counts_next_frame_score(self):
		self.bowling.throw(10)
		self.assertEqual(self.bowling.frame, 1)
		self.assertEqual(self.bowling.score[0], 10)
		self.bowling.throw(5)
		self.bowling.throw(0)
		self.assertEqual(self.bowling.frame, 2)
		self.assertEqual(self.bowling.score[0], 10)
		self.bowling.throw(6)
		self.bowling.throw(3)
		self.assertEqual(self.bowling.frame, 3)
		self.assertEqual(self.bowling.score[0], 24)
		self.assertEqual(self.bowling.score[1], 5)
		self.assertEqual(self.bowling.score[2], 9)

	
	def test_throw_gutterball(self):
		self.bowling.throw(0)
		self.assertEqual(self.bowling.score[0], 0)
		self.assertFalse(self.bowling.first_throw)
		self.assertEqual(self.bowling.frame, 0)

	def test_spare_on_last_frame(self):
		totalExpected = self.throw_to_9th_frame()
		self.bowling.throw(1)
		self.bowling.throw(9)
		self.assertEqual(self.bowling.score[9], totalExpected+10)
		self.assertFalse(self.bowling.first_throw)
		self.assertEqual(self.bowling.frame, 9)

	def test_strike_on_last_frame(self):
		totalExpected = self.throw_to_9th_frame()
		self.bowling.throw(10)
		self.assertEqual(self.bowling.score[9], totalExpected+10)
		self.assertFalse(self.bowling.first_throw)
		self.assertEqual(self.bowling.frame, 9)

	def test_throw_on_11th_frame(self):
		totalExpected = self.throw_to_9th_frame()
		self.bowling.throw(3)
		self.bowling.throw(5)
		self.assertEqual(self.bowling.throw(5), -1)
		self.assertEqual(self.bowling.score[9], totalExpected + 8)
		self.assertFalse(self.bowling.first_throw)
		self.assertEqual(self.bowling.frame, 9)


	def throw_to_9th_frame(self):
		self.bowling.throw(4)
		self.bowling.throw(3)
		self.bowling.throw(2)
		self.bowling.throw(7)
		self.bowling.throw(1)
		self.bowling.throw(0)
		self.bowling.throw(2)
		self.bowling.throw(7)
		self.bowling.throw(4)
		self.bowling.throw(3)
		self.bowling.throw(2)
		self.bowling.throw(7)
		self.bowling.throw(6)
		self.bowling.throw(2)
		self.bowling.throw(3)
		self.bowling.throw(2)
		self.bowling.throw(3)
		self.bowling.throw(2)
		return 60




suite = unittest.TestLoader().loadTestsFromTestCase(BowlingTest)
unittest.TextTestRunner(verbosity=2).run(suite)
