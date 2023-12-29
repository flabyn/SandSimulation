from elements.Solid.moveableSolid.moveableSolid import MoveableSolid
import random

class Sand(MoveableSolid):
    def __init__(self, x,y) -> None:
        super().__init__(x,y)
        self.colour = self.RandomColour((179, 181, 56))