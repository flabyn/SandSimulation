from elements.Element import Element

class EmptyCell(Element):
    def __init__(self, x,y) -> None:
        super().__init__(x,y)

    def step(self,matrix):
        return
    
    def TransferTemp(self, matrix):
        return