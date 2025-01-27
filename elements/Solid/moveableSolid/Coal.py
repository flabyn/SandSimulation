from elements.Solid.moveableSolid.moveableSolid import MoveableSolid
import random
class Coal(MoveableSolid):
    def __init__(self, x,y) -> None:
        super().__init__(x,y)
        self.colour = self.RandomColour((20, 20, 20))
        self.origanlColour = self.colour
        self.friction = 0.80
        self.flameresistance = 0.6
        self.burnrate = 4
    
    def step(self, matrix):
        if self.isIgnited and random.random() < 0.3:
            self.Ignited(matrix)
        return super().step(matrix)
    
    def reciveHeat(self, heat, matrix):
        if self.isIgnited:
            return
        if heat > 10 and random.random() > self.flameresistance:
            self.isIgnited = True
            self.temp = 1000