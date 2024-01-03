from elements.Solid.moveableSolid.moveableSolid import MoveableSolid

class Coal(MoveableSolid):
    def __init__(self, x,y) -> None:
        super().__init__(x,y)
        self.colour = self.RandomColour((20, 20, 20))
        self.friction = 0.80
    
    def step(self, matrix):
        if self.isIgnited:
            self.Ignited()
        return super().step(matrix)