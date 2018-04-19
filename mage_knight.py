import jsonpickle

class Tile:
    pass


class WedgeMap:
    
    def __init__(self):
        self.tiles = [0, 0, 0]

    def __len__(self):
        return len(self.tiles)


class Game:
    
    def __init__(self, source=None):
        self.map = WedgeMap()
