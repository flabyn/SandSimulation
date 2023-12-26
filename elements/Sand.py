from elements.Element import Element

class Sand(Element):
    def __init__(self, x,y) -> None:
        super().__init__(x,y)
        self.colour = (20,100,100)
    
    def step(self):
        return super().step()