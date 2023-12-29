from elements.Gas.Gas import Gas

class Steam(Gas):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)
        self.colour = (179, 198, 230)
        self.viscosity = 0.4