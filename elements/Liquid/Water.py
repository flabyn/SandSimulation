from elements.Liquid.Liquid import Liquid
from elements.ElementTypeShh import ElementType #i dont like this

class Water(Liquid):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)
        self.colour = (20,20,150)
        self.dispersialrate = 4
    
    def reciveHeat(self, heat, matrix):
        if heat > 10:
            matrix.DieAndReplace(self.position,ElementType.STEAM)
