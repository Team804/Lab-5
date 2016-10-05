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

	def testSpareCountsNextFrameScore(self):
		self.bowling.throw(5)
		self.bowling.throw(5)
		self.assertEqual(self.bowling.frame, 1)
		self.bowling.throw(7)
		self.assertEqual(self.bowling.score[0], 17)
		self.assertEqual(self.bowling.score[1], 7)

	def testStrikeMovesToNextFrame(self):
		self.bowling.throw(10)
		self.assertEqual(self.bowling.frame, 1)
		self.bowling.throw(10)
		self.assertEqual(self.bowling.frame, 2)
		self.bowling.throw(5)
		self.assertEqual(self.bowling.frame, 2)
		self.bowling.throw(3)
		self.assertEqual(self.bowling.frame, 3)


	def testStrikeCountsNextFrameScores(self):
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

	def testSpareOnLastFrame(self):

	def testStrikeOnLastFrames(self):

	def testThrowOn11thFrame(self):




suite = unittest.TestLoader().loadTestsFromTestCase(BowlingTest)
unittest.TextTestRunner(verbosity=3).run(suite)
