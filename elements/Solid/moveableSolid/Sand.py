from elements.Solid.moveableSolid.moveableSolid import MoveableSolid

class Sand(MoveableSolid):
    def __init__(self, x,y) -> None:
        super().__init__(x,y)
        self.colour = (179, 181, 56)
    