from elements.Element import Element
from elements.EmptyCell import EmptyCell
class MoveableSolid(Element):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)
    
    def step(self,matrix):
        if self.position[1] == matrix.Matrixsize[1]-1:
            return
        if isinstance(matrix.GetElementAtIndex(self.position[0],self.position[1]+1),EmptyCell):
            matrix.SwapElementsAtIndex(self.position,(self.position[0],self.position[1]+1))

    