# import jsonpickle

class Tile:
    
    def __len__(self):
        return 7


class WedgeMap:
    
    def __init__(self):
        self.tiles = [
            (Tile()),
        ]

    def __len__(self):
        return len(self.tiles)

    #def explorable_spaces(self):
        

class Game:
    
    def __init__(self, source=None):
        self.map = WedgeMap()
