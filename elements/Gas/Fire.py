from elements.Gas.Gas import Gas
from elements.ElementTypeShh import ElementType #i dont like this
import random
class Fire(Gas):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)
        self.colour = self.RandomColour((148, 15, 15),5)
        self.viscosity = 0.5
        self.life = 30
        self.temp = 100
    
    def step(self, matrix):
        self.spreadHeat(matrix)
        return super().step(matrix)

    def lifeStep(self, matrix):
        if self.life == 0:
            if random.random() < 0.2:
                matrix.DieAndReplace(self.position,ElementType.SMOKE)
            else:
                matrix.DieAndReplace(self.position,ElementType.EMPTYCELL)
        else:
            self.colour = (148, 135-(self.life*4), 15)
            self.life -= 1