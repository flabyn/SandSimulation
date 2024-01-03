from elements.Gas.Gas import Gas
from elements.ElementTypeShh import ElementType #i dont like this

class Smoke(Gas):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)
        self.colour = self.RandomColour((82, 74, 74),15)
        self.viscosity = 0.3
        self.life = 60
    
    def lifeStep(self, matrix):
        if self.life == 0:
            matrix.DieAndReplace(self.position,ElementType.EMPTYCELL)
        else:
            self.life -= 1