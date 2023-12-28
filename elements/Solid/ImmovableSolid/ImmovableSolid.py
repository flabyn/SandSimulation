from elements.Solid.Solid import Solid

class ImmovableSolid(Solid):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)