from elements.Element import Element
from elements.EmptyCell import EmptyCell
from elements.Solid.Solid import Solid
from elements.ElementTypeShh import ElementType #i dont like this
import random

class Liquid(Element):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)
        self.dispersialrate = 1+1
    
    def step(self,matrix):
        if self.position[1] == matrix.Matrixsize[1]-1:
            return

        #1 fall if air below

        if isinstance(matrix.GetElementAtIndex(self.position[0],self.position[1]+1),EmptyCell):
            self.velocity = (self.velocity[0],min(self.velocity[1]+1,self.terminal_velocity))
            self.handleVelocityMultiStops(matrix,Solid,Liquid)
            return
        #2 check sides
        valid_positions = []
        if self.position[0] < matrix.Matrixsize[0]-1:
            if isinstance(matrix.GetElementAtIndex(self.position[0]+1,self.position[1]),EmptyCell):
                valid_positions.append(self.Disperisal(matrix,1))
        if self.position[0] > 0:
            if isinstance(matrix.GetElementAtIndex(self.position[0]-1,self.position[1]),EmptyCell):
                valid_positions.append(self.Disperisal(matrix,-1))
        if len(valid_positions)>0:
            matrix.SwapElementsAtIndex(self.position,random.choice(valid_positions))

    def Disperisal(self,matrix,direction):
        if self.position[0]+(self.dispersialrate*direction) > matrix.Matrixsize[0] or self.position[0]+(self.dispersialrate*direction) < 0:
            num = 1
        else:
            num = self.dispersialrate
        for i in range(1*direction,num*direction,1*direction):

            if not isinstance(matrix.GetElementAtIndex(self.position[0]+i,self.position[1]),EmptyCell):
                return (self.position[0]+i-(1*direction),self.position[1])
        return (self.position[0]+(num*direction)-(1*direction),self.position[1])
