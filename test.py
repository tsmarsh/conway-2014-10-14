import unittest
from game import Game 

class TestGame(unittest.TestCase):

	def setUp(self):
		self.game = Game(10, 10)

	def test_can_bring_cell_to_life(self):
		self.assertFalse(self.game.is_alive(0,0))
		self.game.bring_to_life(0,0)
		self.assertTrue(self.game.is_alive(0,0))
		self.assertFalse(self.game.is_alive(0,1))

	def test_can_kill_a_cell(self):
		self.game.bring_to_life(0,0)
		self.game.kill_cell(0,0)
		self.assertFalse(self.game.is_alive(0,0))

	def test_two_neighbors_is_alive(self):
		self.game.bring_to_life(0,0)
		self.game.bring_to_life(0,2)
		self.game.iterate()
		self.assertTrue(self.game.is_alive(0,1))

	def test_returns_living_neighbors(self):
		self.game.bring_to_life(0,0)
		self.game.bring_to_life(0,2)
		self.assertEqual(self.game.count_neighbors(0,1), 2)

	def test_kills_overcrowded_cells(self):
		self.game.bring_to_life(0,1)
		self.game.bring_to_life(1,0)
		self.game.bring_to_life(1,1)
		self.game.bring_to_life(1,2)
		self.game.bring_to_life(2,1)
		self.game.iterate()
		self.assertFalse(self.game.is_alive(1,1))

	def test_cell_with_less_than_2_neigh_dies(self):
		self.game.bring_to_life(0,1)
		self.game.bring_to_life(0,0)
		self.game.iterate()
		self.assertFalse(self.game.is_alive(0,1))
		


if __name__ == '__main__':
    unittest.main()
