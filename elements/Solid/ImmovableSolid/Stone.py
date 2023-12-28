from elements.Solid.ImmovableSolid.ImmovableSolid import ImmovableSolid

class Stone(ImmovableSolid):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)
        self.colour = (40,40,40)
