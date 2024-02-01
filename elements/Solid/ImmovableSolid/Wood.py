from elements.Solid.ImmovableSolid.ImmovableSolid import ImmovableSolid
import random

class Wood(ImmovableSolid):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)
        self.colour = self.RandomColour((74, 48, 15))
        self.origanlColour = self.colour
        self.flameresistance = 0.4
        self.burnrate = 10
    
    def step(self, matrix):
        if self.isIgnited and random.random() < 0.3:
            self.Ignited(matrix)
        return super().step(matrix)
    
    def reciveHeat(self, heat, matrix):
        if self.isIgnited:
            return
        if heat > 10 and random.random() > self.flameresistance:
            self.isIgnited = True
            self.temp = heat