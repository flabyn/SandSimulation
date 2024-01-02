from elements.Liquid.Liquid import Liquid

class Water(Liquid):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)
        self.colour = (20,20,150)
        self.dispersialrate = 4