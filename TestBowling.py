import unittest

from Bowling import Bowling


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.bowling_game = Bowling()

    @unittest.skip
    def test_environment(self):
        self.assertEqual(True, False)

    def test_score_zero(self):
        self.assertEqual(0, self.bowling_game.get_score())

    def test_score_one(self):
        self.bowling_game.num_balls_hit(1)
        self.bowling_game.num_balls_hit(0)
        self.assertEqual(1, self.bowling_game.get_score())

    def test_score_strike(self):
        self.bowling_game.num_balls_hit(10)  # Frame 1 strike = 10 + 1 + 2 = 13
        self.bowling_game.num_balls_hit(0)   # Frame 1 strike
        self.bowling_game.num_balls_hit(1)   # Frame 2 normal 1 + 2 = 3 + 13 = 16
        self.bowling_game.num_balls_hit(2)
        self.assertEqual(16, self.bowling_game.get_score())

    def test_score_spare(self):
        self.bowling_game.num_balls_hit(9)  # Frame 1 = 9
        self.bowling_game.num_balls_hit(1)  # Frame 1 spare = 9 + 1 = 10 + 2 = 12
        self.bowling_game.num_balls_hit(2)  # Frame 2 = 12 + 2 = 14
        self.bowling_game.num_balls_hit(0)  # Frame 2 = 14 + 0 = 14
        self.assertEqual(14, self.bowling_game.get_score())


if __name__ == '__main__':
    unittest.main()
