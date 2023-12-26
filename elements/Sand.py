from elements.Element import Element

class Sand(Element):
    def __init__(self, x,y) -> None:
        super().__init__(x,y)
    
    def step(self):
        return super().step()