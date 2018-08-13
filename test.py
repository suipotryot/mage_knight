import unittest

from mage_knight import Game, WedgeMap, Tile

class TestGame(unittest.TestCase):

    def test_init_should_add_map(self):
        game = Game()

        result_map = game.map

        self.assertIsInstance(result_map, WedgeMap)


class TestWedgeMap(unittest.TestCase):

    def test_init_should_add_1_tile(self):
        tested_map = WedgeMap()

        result = len(tested_map)

        self.assertEqual(result, 1)

    def test_explorable_starting_spaces(self):
        tested_map = WedgeMap()

        result = tested_map.explorable_spaces()

        self.assertEqual(result, [(3, 0), (3, 1), (2, 2), (1, 3)])

    # def test_explorable_spaces(self):
    #     tested_map = WedgeMap()

    #     result = tested_map.explorable_spaces()

    #     self.assertEqual(result, [(6, -1), (6, 0), (5, 1), (4, 2), (4, 3), (3, 4), (2, 5)])


class TestTile(unittest.TestCase):

    def test_init_should_add_7_spaces(self):
        tile = Tile()

        result = len(tile)

        self.assertEqual(result, 7)
