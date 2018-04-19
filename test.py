import unittest

from mage_knight import Game, WedgeMap, Tile

class TestGame(unittest.TestCase):

    def test_init_should_add_map(self):
        game = Game()

        result_map = game.map

        self.assertIsInstance(result_map, WedgeMap)


class TestWedgeMap(unittest.TestCase):

    def test_init_should_add_3_tiles(self):
        tested_map = WedgeMap()

        result = len(tested_map)

        self.assertEqual(result, 3)
        for 


class TestTile(unittest.TestCase):

    def test_init_should_add_7_spaces(self):
        tile = Tile()

        result = len(tile)

        self.assertEqual(result, 7)
